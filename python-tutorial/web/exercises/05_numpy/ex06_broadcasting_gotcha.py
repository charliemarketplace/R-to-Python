"""
EXERCISE 6: Broadcasting Gotcha - Shape Surprises

THE GOTCHA:
    a = np.array([[1], [2], [3]])  # Shape (3, 1)
    b = np.array([10, 20, 30])     # Shape (3,)

    # What's (a + b).shape?
    # Answer: (3, 3)! An outer-product-like result!

Broadcasting alignment (right to left):
    (3, 1) + (3,) -> (3, 1) + (1, 3) -> (3, 3)

The (3,) is treated as (1, 3), then both dimensions broadcast!

This is DIFFERENT from R, which would recycle:
    R:      matrix(1:3) + c(10, 20, 30)  # Error or column recycling

To add as columns (element-wise):
    Option 1: Make b a column: b.reshape(-1, 1) or b[:, np.newaxis]
    Option 2: Make a a row: a.flatten() or a.ravel()

TASK:
Given the column vector and row vector:
1. Predict and create the result of col + row (outer-product-like)
2. Add them element-wise as columns (result shape should be (3, 1))
3. Add them element-wise as rows (result shape should be (1, 3))
"""
import numpy as np

col = np.array([[1], [2], [3]])  # Shape (3, 1)
row = np.array([10, 20, 30])     # Shape (3,)

# ---- YOUR CODE HERE ----
# Task 1: What is col + row? (it broadcasts to 3x3!)
outer_sum = None  # Should be 3x3 matrix

# Task 2: Add as columns (both should be (3, 1), result (3, 1))
# Need to reshape row to (3, 1)
col_wise_sum = None

# Task 3: Add as rows (both should be (1, 3), result (1, 3))
# Need to reshape col to (1, 3)
row_wise_sum = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Outer sum (3x3)")
    expected_outer = np.array([
        [11, 21, 31],
        [12, 22, 32],
        [13, 23, 33]
    ])
    check(outer_sum, expected=expected_outer,
          hint="col + row broadcasts to (3,3): each col element + each row element")

    print("\nTask 2: Column-wise sum (3x1)")
    check(col_wise_sum, expected=np.array([[11], [22], [33]]),
          hint="col + row.reshape(-1, 1) or col + row[:, np.newaxis]")

    print("\nTask 3: Row-wise sum (1x3)")
    check(row_wise_sum, expected=np.array([[11, 22, 33]]),
          hint="col.T + row or col.flatten() + row")
