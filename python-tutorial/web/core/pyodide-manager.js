// PyodideManager - handles Pyodide runtime and code execution

class PyodideManager {
  constructor() {
    this.pyodide = null;
    this.loadedPackages = new Set();
    this.loading = false;
    this.initPromise = null;
  }

  /**
   * Initialize Pyodide runtime. Call on landing page.
   * Returns cached instance if already initialized.
   */
  async init() {
    if (this.pyodide) return this.pyodide;
    if (this.initPromise) return this.initPromise;

    this.initPromise = (async () => {
      this.loading = true;

      // loadPyodide is loaded from CDN in HTML
      this.pyodide = await loadPyodide({
        indexURL: 'https://cdn.jsdelivr.net/pyodide/v0.24.1/full/',
      });

      // Setup stdout/stderr capture
      await this.pyodide.runPythonAsync(`
import sys
from io import StringIO

class OutputCapture:
    def __init__(self):
        self.stdout = StringIO()
        self.stderr = StringIO()

    def reset(self):
        self.stdout = StringIO()
        self.stderr = StringIO()
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def get_output(self):
        return {
            'stdout': self.stdout.getvalue(),
            'stderr': self.stderr.getvalue(),
        }

_capture = OutputCapture()
sys.stdout = _capture.stdout
sys.stderr = _capture.stderr
      `);

      this.loading = false;
      return this.pyodide;
    })();

    return this.initPromise;
  }

  /**
   * Load packages if not already loaded.
   * Returns list of newly loaded packages.
   */
  async ensurePackages(packages, onProgress = null) {
    await this.init();

    const needed = packages.filter(p => !this.loadedPackages.has(p));
    if (needed.length === 0) return [];

    if (onProgress) onProgress({ phase: 'downloading', packages: needed });

    await this.pyodide.loadPackage(needed, {
      messageCallback: (msg) => {
        if (onProgress) onProgress({ phase: 'loading', message: msg });
      },
    });

    needed.forEach(p => this.loadedPackages.add(p));

    if (onProgress) onProgress({ phase: 'complete', packages: needed });

    return needed;
  }

  /**
   * Execute user code safely.
   * Returns { success, result, stdout, stderr, error }
   */
  async runCode(code, timeoutMs = 30000) {
    await this.init();

    // Reset output capture
    await this.pyodide.runPythonAsync('_capture.reset()');

    try {
      // Execute user code
      const result = await this.pyodide.runPythonAsync(code);

      // Get captured output
      const output = this.pyodide.runPython('_capture.get_output()').toJs();

      return {
        success: true,
        result: result?.toString?.() ?? result,
        stdout: output.get('stdout'),
        stderr: output.get('stderr'),
        error: null,
      };
    } catch (err) {
      const output = this.pyodide.runPython('_capture.get_output()').toJs();

      return {
        success: false,
        result: null,
        stdout: output.get('stdout'),
        stderr: output.get('stderr'),
        error: this.formatError(err),
      };
    }
  }

  /**
   * Run grading for an exercise.
   * Runs the actual grading code from the exercise file.
   */
  async grade(setupCode, userCode, gradingCode, hint = null) {
    // Define a simple check() function that mimics the grader
    const checkFunction = `
import numpy as np

def check(got, expected, hint=None, rtol=1e-6):
    """Simple check function for grading."""
    try:
        # Handle None
        if expected is None and got is None:
            print("[PASS] Correct!")
            return True
        if expected is None or got is None:
            print(f"[FAIL] Expected {expected!r}, got {got!r}")
            return False

        # NumPy arrays
        if isinstance(expected, np.ndarray):
            if not isinstance(got, np.ndarray):
                print(f"[FAIL] Expected numpy array, got {type(got).__name__}")
                return False
            np.testing.assert_allclose(got, expected, rtol=rtol)
            print("[PASS] Correct!")
            return True

        # Lists - compare element by element
        if isinstance(expected, list):
            if got != expected:
                print(f"[FAIL] Expected {expected!r}, got {got!r}")
                return False
            print("[PASS] Correct!")
            return True

        # Floats with tolerance
        if isinstance(expected, float):
            if abs(got - expected) > rtol * max(abs(expected), 1):
                print(f"[FAIL] Expected ~{expected}, got {got}")
                return False
            print("[PASS] Correct!")
            return True

        # Default equality
        if got != expected:
            print(f"[FAIL] Expected {expected!r}, got {got!r}")
            return False
        print("[PASS] Correct!")
        return True

    except AssertionError as e:
        print(f"[FAIL] {e}")
        return False
    except Exception as e:
        print(f"[FAIL] Error: {e}")
        return False

def check_type(got, expected_type, hint=None):
    if isinstance(got, expected_type):
        print(f"[PASS] Correct type: {type(got).__name__}")
        return True
    print(f"[FAIL] Expected {expected_type}, got {type(got).__name__}")
    return False

def check_plot(fig, check_type="scatter", hint=None):
    try:
        if fig is None:
            print("[FAIL] Figure is None")
            return False
        if not hasattr(fig, 'data') or len(fig.data) == 0:
            print("[FAIL] Figure has no data")
            return False
        types = [t.type for t in fig.data]
        if check_type.lower() in [t.lower() for t in types]:
            print(f"[PASS] Plot looks good! Found {len(fig.data)} trace(s)")
            return True
        print(f"[FAIL] Expected '{check_type}' trace, found: {types}")
        return False
    except Exception as e:
        print(f"[FAIL] {e}")
        return False

def check_model(model, param, expected, rtol=0.1):
    try:
        if not hasattr(model, 'params'):
            print("[FAIL] Not a statsmodels result object")
            return False
        if param not in model.params:
            print(f"[FAIL] Parameter '{param}' not found")
            return False
        actual = model.params[param]
        if abs(actual - expected) / max(abs(expected), 1e-10) > rtol:
            print(f"[FAIL] Coefficient '{param}': expected ~{expected:.4f}, got {actual:.4f}")
            return False
        print(f"[PASS] Coefficient '{param}' correct: {actual:.4f}")
        return True
    except Exception as e:
        print(f"[FAIL] {e}")
        return False
`;

    // Run setup + user code + grading code together
    const fullCode = checkFunction + '\n' + setupCode + '\n' + userCode + '\n' + gradingCode;
    const result = await this.runCode(fullCode);

    // Count passes and failures from output
    const passedCount = (result.stdout.match(/\[PASS\]/g) || []).length;
    const failedCount = (result.stdout.match(/\[FAIL\]/g) || []).length;

    // Check for code errors
    if (!result.success && passedCount === 0 && failedCount === 0) {
      return {
        passed: false,
        message: result.error,
        hint: hint,
        stdout: result.stdout,
        passedCount: 0,
        failedCount: 1,
      };
    }

    return {
      passed: failedCount === 0 && passedCount > 0,
      message: result.stdout,
      hint: failedCount > 0 ? hint : null,
      stdout: result.stdout,
      passedCount,
      failedCount,
    };
  }

  /**
   * Get a Python variable's value.
   */
  getVariable(name) {
    try {
      const value = this.pyodide.globals.get(name);
      return value?.toJs?.() ?? value;
    } catch {
      return undefined;
    }
  }

  /**
   * Check if packages are loaded.
   */
  hasPackages(packages) {
    return packages.every(p => this.loadedPackages.has(p));
  }

  formatError(err) {
    const msg = err.message || String(err);
    const lines = msg.split('\n');

    // Find the actual error line (skip Pyodide internals)
    const errorIdx = lines.findIndex(l =>
      l.includes('Error:') || l.includes('Exception:')
    );

    if (errorIdx >= 0) {
      return lines.slice(Math.max(0, errorIdx - 2)).join('\n');
    }
    return msg;
  }

  formatAssertionError(err) {
    const msg = err.message || String(err);

    if (msg.includes('AssertionError')) {
      const match = msg.match(/AssertionError:?\s*(.*)/s);
      return match ? match[1].trim().split('\n')[0] : 'Assertion failed';
    }
    return msg.split('\n')[0];
  }
}

// Singleton export
export const pyodide = new PyodideManager();
