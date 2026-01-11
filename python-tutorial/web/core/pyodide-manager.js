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

    // Packages that need micropip (not in Pyodide's built-in packages)
    const micropipPackages = ['polars'];
    const builtinPackages = needed.filter(p => !micropipPackages.includes(p));
    const pipPackages = needed.filter(p => micropipPackages.includes(p));

    // Load built-in packages
    if (builtinPackages.length > 0) {
      await this.pyodide.loadPackage(builtinPackages, {
        messageCallback: (msg) => {
          if (onProgress) onProgress({ phase: 'loading', message: msg });
        },
      });
    }

    // Load micropip packages
    if (pipPackages.length > 0) {
      if (onProgress) onProgress({ phase: 'loading', message: 'Loading micropip...' });
      await this.pyodide.loadPackage('micropip');
      const micropip = this.pyodide.pyimport('micropip');

      for (const pkg of pipPackages) {
        if (onProgress) onProgress({ phase: 'loading', message: `Installing ${pkg} via pip...` });
        await micropip.install(pkg);
      }
    }

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
  async grade(setupCode, userCode, postUserCode, gradingCode, hint = null) {
    // Simple check function - just equality comparison
    const checkFunction = `
def check(got, expected, hint=None, rtol=1e-6):
    """Check if got equals expected."""
    if got == expected:
        print("[PASS] Correct!")
        return True
    print(f"[FAIL] Expected {expected!r}, got {got!r}")
    return False

def check_type(got, expected_type, hint=None):
    """Check if got is the expected type."""
    if isinstance(got, expected_type):
        print(f"[PASS] Correct type: {type(got).__name__}")
        return True
    print(f"[FAIL] Expected {expected_type.__name__}, got {type(got).__name__}")
    return False

def check_exists(obj, hint=None):
    """Check that something was created (not None, runs without error)."""
    if obj is not None:
        print("[PASS] Created successfully!")
        return True
    print("[FAIL] Object is None")
    return False
`;

    // Run setup + user code + post-user code + grading code together
    const fullCode = checkFunction + '\n' + setupCode + '\n' + userCode + '\n' + (postUserCode || '') + '\n' + gradingCode;
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
