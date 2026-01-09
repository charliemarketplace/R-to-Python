"""
EXERCISE 4: Reshaping Arrays

R vs Python:
    R:      matrix(1:12, nrow=3, ncol=4)      # Fill by column!
            matrix(1:12, nrow=3, byrow=TRUE)   # Fill by row
    Python: np.arange(12).reshape(3, 4)        # Fill by row (default)

Reshaping functions:
    arr.reshape(new_shape)  # Returns view with new shape
    arr.ravel()             # Flatten to 1D (returns view)
    arr.flatten()           # Flatten to 1D (returns copy)
    arr.T                   # Transpose

The -1 trick:
    arr.reshape(3, -1)  # 3 rows, auto-calculate columns
    arr.reshape(-1)     # Flatten

Important: Reshaping returns a VIEW, not a copy!
Changes to the reshaped array affect the original.

TASK:
Given a 1D array of 12 elements:
1. Reshape to 3x4 matrix
2. Reshape to 4x3 matrix
3. Reshape to 2x6 matrix
4. Transpose the 3x4 matrix to get 4x3
"""
import numpy as np

arr = np.arange(1, 13)  # [1, 2, 3, ..., 12]

# ---- YOUR CODE HERE ----
mat_3x4 = None   # Shape (3, 4)
mat_4x3 = None   # Shape (4, 3)
mat_2x6 = None   # Shape (2, 6)
transposed = None  # Transpose of 3x4 matrix
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: 3x4 matrix")
    expected_3x4 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    check(mat_3x4, expected=expected_3x4,
          hint="arr.reshape(3, 4)")

    print("\nTask 2: 4x3 matrix")
    expected_4x3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
    check(mat_4x3, expected=expected_4x3,
          hint="arr.reshape(4, 3)")

    print("\nTask 3: 2x6 matrix")
    expected_2x6 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
    check(mat_2x6, expected=expected_2x6,
          hint="arr.reshape(2, 6) or arr.reshape(2, -1)")

    print("\nTask 4: Transposed (4x3)")
    expected_trans = np.array([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]])
    check(transposed, expected=expected_trans,
          hint="mat_3x4.T")
