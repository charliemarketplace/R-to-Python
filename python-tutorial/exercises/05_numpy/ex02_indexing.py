"""
EXERCISE 2: NumPy Array Indexing

R vs Python:
    R:      mat[1, 2]      # Row 1, col 2 (1-indexed)
    Python: arr[0, 1]      # Row 0, col 1 (0-indexed)

NumPy indexing:
    arr[i]         # 1D: element at index i
    arr[i, j]      # 2D: row i, column j
    arr[i][j]      # Also works but less efficient

Getting rows and columns:
    arr[0]         # First row (returns 1D array)
    arr[:, 0]      # First column (returns 1D array)
    arr[0:2]       # First two rows
    arr[:, 0:2]    # First two columns

R vs Python indexing example:
    R:      mat[1, ]   # First row
            mat[, 1]   # First column
    Python: arr[0]     # First row (or arr[0, :])
            arr[:, 0]  # First column

TASK:
Given the 3x4 matrix:
1. Get the element at row 1, column 2 (0-indexed)
2. Get the entire second row
3. Get the entire third column
4. Get the 2x2 submatrix from top-left corner
"""
import numpy as np

matrix = np.array([
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9, 10, 11, 12]
])

# ---- YOUR CODE HERE ----
element = None   # Element at row 1, col 2 -> should be 7
row = None       # Second row -> [5, 6, 7, 8]
column = None    # Third column -> [3, 7, 11]
submatrix = None # Top-left 2x2 -> [[1,2], [5,6]]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Element at [1, 2]")
    check(element, expected=7,
          hint="matrix[1, 2] - row 1 is [5,6,7,8], col 2 is 7")

    print("\nTask 2: Second row")
    check(row, expected=np.array([5, 6, 7, 8]),
          hint="matrix[1] or matrix[1, :]")

    print("\nTask 3: Third column")
    check(column, expected=np.array([3, 7, 11]),
          hint="matrix[:, 2] - all rows, column index 2")

    print("\nTask 4: Top-left 2x2")
    check(submatrix, expected=np.array([[1, 2], [5, 6]]),
          hint="matrix[0:2, 0:2] or matrix[:2, :2]")
