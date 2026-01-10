"""
EXERCISE 8: Vectorized Operations

R vs Python:
    R:      x^2, sqrt(x), log(x), exp(x)  # Vectorized
    Python: x**2, np.sqrt(x), np.log(x), np.exp(x)  # Also vectorized!

NumPy's power comes from vectorized operations:
- Operations apply element-wise to entire arrays
- Much faster than Python loops
- Similar to R's vectorization

Universal functions (ufuncs):
    np.sqrt(arr)     # Square root
    np.exp(arr)      # e^x
    np.log(arr)      # Natural log
    np.log10(arr)    # Base-10 log
    np.sin(arr)      # Trigonometric
    np.abs(arr)      # Absolute value
    np.round(arr)    # Round

Array arithmetic:
    arr + arr2, arr - arr2, arr * arr2, arr / arr2
    arr ** 2, arr // 2 (floor div), arr % 2 (modulo)

Comparison (returns boolean array):
    arr > 5, arr == 0, arr != val

TASK:
Given an array of values:
1. Calculate the z-scores: (x - mean) / std
2. Calculate e^x for each element
3. Calculate log base 10 of each element
4. Round each element to 1 decimal place
"""
import numpy as np

values = np.array([1.0, 2.5, 3.0, 4.5, 5.0, 6.5, 7.0, 8.5, 9.0, 10.0])

# ---- YOUR CODE HERE ----
# Task 1: Z-scores (standardize)
z_scores = None

# Task 2: Exponential
exponentials = None

# Task 3: Log base 10
log10_values = None

# Task 4: Round to 1 decimal
rounded = None  # Round the z_scores to 1 decimal place
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Z-scores")
    expected_z = (values - values.mean()) / values.std()
    check(z_scores, expected=expected_z, rtol=0.01,
          hint="(values - values.mean()) / values.std()")

    print("\nTask 2: Exponentials")
    check(exponentials, expected=np.exp(values), rtol=0.01,
          hint="np.exp(values)")

    print("\nTask 3: Log base 10")
    check(log10_values, expected=np.log10(values), rtol=0.01,
          hint="np.log10(values)")

    print("\nTask 4: Rounded z-scores")
    check(rounded, expected=np.round(expected_z, 1), rtol=0.01,
          hint="np.round(z_scores, 1)")
