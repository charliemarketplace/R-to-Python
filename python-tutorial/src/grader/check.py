"""Universal grading utilities for Python tutorial exercises."""

import numpy as np
import pandas as pd
import polars as pl
from typing import Any, Callable, Type


def check(got: Any, expected: Any, hint: str | None = None, rtol: float = 1e-6) -> bool:
    """
    Universal checker - handles scalars, arrays, DataFrames, and more.

    Parameters
    ----------
    got : Any
        The student's answer
    expected : Any
        The expected answer
    hint : str, optional
        Hint to display if answer is incorrect
    rtol : float
        Relative tolerance for numeric comparisons

    Returns
    -------
    bool
        True if correct, False otherwise
    """
    try:
        if expected is None and got is None:
            print("[PASS] Correct!")
            return True

        if expected is None or got is None:
            raise AssertionError(f"Expected {expected!r}, got {got!r}")

        # pandas DataFrame
        if isinstance(expected, pd.DataFrame):
            if not isinstance(got, pd.DataFrame):
                raise AssertionError(f"Expected pandas DataFrame, got {type(got).__name__}")
            pd.testing.assert_frame_equal(got, expected, check_dtype=False, rtol=rtol)

        # pandas Series
        elif isinstance(expected, pd.Series):
            if not isinstance(got, pd.Series):
                raise AssertionError(f"Expected pandas Series, got {type(got).__name__}")
            pd.testing.assert_series_equal(got, expected, check_dtype=False, rtol=rtol)

        # Polars DataFrame
        elif isinstance(expected, pl.DataFrame):
            if not isinstance(got, pl.DataFrame):
                raise AssertionError(f"Expected Polars DataFrame, got {type(got).__name__}")
            assert got.equals(expected), "Polars DataFrames don't match"

        # Polars Series
        elif isinstance(expected, pl.Series):
            if not isinstance(got, pl.Series):
                raise AssertionError(f"Expected Polars Series, got {type(got).__name__}")
            assert got.equals(expected), "Polars Series don't match"

        # NumPy array
        elif isinstance(expected, np.ndarray):
            if not isinstance(got, np.ndarray):
                raise AssertionError(f"Expected numpy array, got {type(got).__name__}")
            np.testing.assert_allclose(got, expected, rtol=rtol)

        # Float comparison with tolerance
        elif isinstance(expected, float):
            if not isinstance(got, (int, float, np.number)):
                raise AssertionError(f"Expected numeric type, got {type(got).__name__}")
            if not np.isclose(got, expected, rtol=rtol):
                raise AssertionError(f"Expected ~{expected}, got {got}")

        # List comparison (element-wise for numeric)
        elif isinstance(expected, list):
            if not isinstance(got, list):
                raise AssertionError(f"Expected list, got {type(got).__name__}")
            if len(got) != len(expected):
                raise AssertionError(f"Expected list of length {len(expected)}, got length {len(got)}")
            for i, (g, e) in enumerate(zip(got, expected)):
                if isinstance(e, float):
                    if not np.isclose(g, e, rtol=rtol):
                        raise AssertionError(f"Element {i}: expected ~{e}, got {g}")
                elif g != e:
                    raise AssertionError(f"Element {i}: expected {e!r}, got {g!r}")

        # Dict comparison
        elif isinstance(expected, dict):
            if not isinstance(got, dict):
                raise AssertionError(f"Expected dict, got {type(got).__name__}")
            if set(got.keys()) != set(expected.keys()):
                missing = set(expected.keys()) - set(got.keys())
                extra = set(got.keys()) - set(expected.keys())
                msg = ""
                if missing:
                    msg += f"Missing keys: {missing}. "
                if extra:
                    msg += f"Extra keys: {extra}."
                raise AssertionError(msg)
            for k in expected:
                if isinstance(expected[k], float):
                    if not np.isclose(got[k], expected[k], rtol=rtol):
                        raise AssertionError(f"Key '{k}': expected ~{expected[k]}, got {got[k]}")
                elif got[k] != expected[k]:
                    raise AssertionError(f"Key '{k}': expected {expected[k]!r}, got {got[k]!r}")

        # Set comparison
        elif isinstance(expected, set):
            if not isinstance(got, set):
                raise AssertionError(f"Expected set, got {type(got).__name__}")
            if got != expected:
                missing = expected - got
                extra = got - expected
                msg = ""
                if missing:
                    msg += f"Missing: {missing}. "
                if extra:
                    msg += f"Extra: {extra}."
                raise AssertionError(msg)

        # Tuple comparison
        elif isinstance(expected, tuple):
            if not isinstance(got, tuple):
                raise AssertionError(f"Expected tuple, got {type(got).__name__}")
            if len(got) != len(expected):
                raise AssertionError(f"Expected tuple of length {len(expected)}, got length {len(got)}")
            for i, (g, e) in enumerate(zip(got, expected)):
                if isinstance(e, float):
                    if not np.isclose(g, e, rtol=rtol):
                        raise AssertionError(f"Element {i}: expected ~{e}, got {g}")
                elif g != e:
                    raise AssertionError(f"Element {i}: expected {e!r}, got {g!r}")

        # Default equality check
        else:
            assert got == expected, f"Expected {expected!r}, got {got!r}"

        print("[PASS] Correct!")
        return True

    except AssertionError as e:
        print(f"[FAIL] Not quite. {e}")
        if hint:
            print(f"  Hint: {hint}")
        return False


def check_model(model: Any, param: str, expected: float, rtol: float = 0.1) -> bool:
    """
    Check statsmodels coefficient within tolerance.

    Parameters
    ----------
    model : statsmodels results object
        Fitted model with .params attribute
    param : str
        Name of coefficient to check
    expected : float
        Expected coefficient value
    rtol : float
        Relative tolerance (default 0.1 = 10%)

    Returns
    -------
    bool
        True if correct, False otherwise
    """
    try:
        if not hasattr(model, 'params'):
            raise ValueError("Not a statsmodels results object (no .params attribute)")

        if param not in model.params:
            available = list(model.params.index)
            raise AssertionError(f"Parameter '{param}' not found. Available: {available}")

        actual = model.params[param]

        if not np.isclose(actual, expected, rtol=rtol):
            raise AssertionError(
                f"Coefficient '{param}': expected ~{expected:.4f}, got {actual:.4f}"
            )

        print(f"[PASS] Coefficient '{param}' correct: {actual:.4f}")
        return True

    except (AssertionError, ValueError) as e:
        print(f"[FAIL] {e}")
        return False


def check_plot(fig: Any, check_type: str = "scatter", hint: str | None = None) -> bool:
    """
    Basic check that a plotly figure exists and has expected trace type.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        The figure to check
    check_type : str
        Expected trace type (scatter, bar, histogram, box, heatmap, etc.)
    hint : str, optional
        Hint to display if check fails

    Returns
    -------
    bool
        True if correct, False otherwise
    """
    try:
        # Check if it's a plotly figure
        fig_type = type(fig).__module__
        if not fig_type.startswith('plotly'):
            raise AssertionError(f"Expected plotly Figure, got {type(fig).__name__}")

        # Check for data
        if not hasattr(fig, 'data') or len(fig.data) == 0:
            raise AssertionError("Figure has no data traces")

        # Check trace type
        trace_types = [trace.type for trace in fig.data]
        if check_type.lower() not in [t.lower() for t in trace_types]:
            raise AssertionError(
                f"Expected '{check_type}' trace, found: {trace_types}"
            )

        print(f"[PASS] Plot looks good! Found {len(fig.data)} trace(s) of type(s): {trace_types}")
        return True

    except AssertionError as e:
        print(f"[FAIL] {e}")
        if hint:
            print(f"  Hint: {hint}")
        return False


def check_type(got: Any, expected_type: Type | tuple, hint: str | None = None) -> bool:
    """
    Check that a value is of the expected type.

    Parameters
    ----------
    got : Any
        The value to check
    expected_type : type or tuple of types
        Expected type(s)
    hint : str, optional
        Hint to display if check fails

    Returns
    -------
    bool
        True if correct, False otherwise
    """
    try:
        if not isinstance(got, expected_type):
            type_name = (expected_type.__name__ if isinstance(expected_type, type)
                        else " or ".join(t.__name__ for t in expected_type))
            raise AssertionError(f"Expected {type_name}, got {type(got).__name__}")

        print(f"[PASS] Correct type: {type(got).__name__}")
        return True

    except AssertionError as e:
        print(f"[FAIL] {e}")
        if hint:
            print(f"  Hint: {hint}")
        return False


def check_error(func: Callable, error_type: Type[Exception], hint: str | None = None) -> bool:
    """
    Check that a function raises the expected error.

    Parameters
    ----------
    func : callable
        A function that should raise an error when called
    error_type : Exception type
        The expected exception type
    hint : str, optional
        Hint to display if check fails

    Returns
    -------
    bool
        True if correct error raised, False otherwise
    """
    try:
        func()
        raise AssertionError(f"Expected {error_type.__name__} to be raised, but no error occurred")
    except error_type:
        print(f"[PASS] Correctly raises {error_type.__name__}")
        return True
    except Exception as e:
        print(f"[FAIL] Expected {error_type.__name__}, got {type(e).__name__}: {e}")
        if hint:
            print(f"  Hint: {hint}")
        return False
