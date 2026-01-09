"""Execute user code safely in subprocess."""

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from dataclasses import dataclass


@dataclass
class ExecutionResult:
    """Result of code execution."""
    success: bool
    output: str
    error: str
    passed: bool
    failed_count: int
    passed_count: int


def execute_exercise(
    exercise_path: Path,
    user_code: str,
    project_root: Path,
    timeout: int = 30
) -> ExecutionResult:
    """
    Execute exercise with user code substituted.

    Strategy:
    1. Read original exercise file
    2. Replace the user code section
    3. Write to temp file
    4. Run with subprocess
    5. Parse output for [PASS]/[FAIL]
    """
    # Read original file
    original = exercise_path.read_text(encoding='utf-8')

    # Find and replace user code section
    user_start = "# ---- YOUR CODE HERE ----"
    user_end = "# ---- END YOUR CODE ----"

    start_idx = original.find(user_start)
    end_idx = original.find(user_end)

    if start_idx == -1 or end_idx == -1:
        return ExecutionResult(
            success=False,
            output="",
            error="Invalid exercise format: markers not found",
            passed=False,
            failed_count=0,
            passed_count=0
        )

    # Construct modified code
    modified = (
        original[:start_idx + len(user_start)] +
        "\n" + user_code + "\n" +
        original[end_idx:]
    )

    # Write to temp file
    with tempfile.NamedTemporaryFile(
        mode='w',
        suffix='.py',
        delete=False,
        encoding='utf-8'
    ) as f:
        f.write(modified)
        temp_path = Path(f.name)

    try:
        # Set up environment with PYTHONPATH
        env = os.environ.copy()
        src_path = str(project_root / "src")
        if "PYTHONPATH" in env:
            env["PYTHONPATH"] = src_path + os.pathsep + env["PYTHONPATH"]
        else:
            env["PYTHONPATH"] = src_path

        # Run in subprocess
        result = subprocess.run(
            [sys.executable, str(temp_path)],
            capture_output=True,
            text=True,
            timeout=timeout,
            cwd=str(project_root),
            env=env
        )

        output = result.stdout
        error = result.stderr

        # Count passes and failures
        passed_count = len(re.findall(r'\[PASS\]', output))
        failed_count = len(re.findall(r'\[FAIL\]', output))

        # Overall pass: at least one pass and no failures
        all_passed = passed_count > 0 and failed_count == 0

        return ExecutionResult(
            success=True,
            output=output,
            error=error,
            passed=all_passed,
            failed_count=failed_count,
            passed_count=passed_count
        )

    except subprocess.TimeoutExpired:
        return ExecutionResult(
            success=False,
            output="",
            error=f"Execution timed out after {timeout} seconds. Check for infinite loops.",
            passed=False,
            failed_count=0,
            passed_count=0
        )
    except Exception as e:
        return ExecutionResult(
            success=False,
            output="",
            error=str(e),
            passed=False,
            failed_count=0,
            passed_count=0
        )
    finally:
        temp_path.unlink(missing_ok=True)
