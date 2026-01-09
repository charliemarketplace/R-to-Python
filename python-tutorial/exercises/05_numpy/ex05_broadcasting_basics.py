"""
EXERCISE 5: Broadcasting Basics

R vs Python:
    R:      x + 1  # Adds 1 to each element (recycling)
    Python: arr + 1  # Same! Broadcasting

Broadcasting is how NumPy handles operations between arrays
of different shapes. It's similar to R's recycling but with rules.

Simple broadcasting:
    arr = np.array([1, 2, 3])
    arr + 10        # [11, 12, 13] - scalar broadcast
    arr * 2         # [2, 4, 6]

The rule: Dimensions are compared from RIGHT to LEFT.
Dimensions are compatible if:
1. They are equal, OR
2. One of them is 1

Example:
    (3, 4) + (4,)   -> OK! (4,) broadcasts to (3, 4)
    (3, 4) + (3,)   -> ERROR! 4 != 3

TASK:
1. Add 10 to every element of arr1
2. Multiply every element of arr2 by 2
3. Add row_to_add to each row of matrix
4. Normalize matrix columns (subtract column mean from each column)
"""
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_to_add = np.array([10, 20, 30])

# ---- YOUR CODE HERE ----
# Task 1: Add 10 to arr1
result1 = None

# Task 2: Multiply arr2 by 2
result2 = None

# Task 3: Add row_to_add to each row of matrix
result3 = None

# Task 4: Subtract column means from matrix (center each column)
# column_means should be [4, 5, 6]
# result4[0] should be [1-4, 2-5, 3-6] = [-3, -3, -3]
column_means = None  # Calculate first
result4 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Add 10")
    check(result1, expected=np.array([11, 12, 13, 14, 15]))

    print("\nTask 2: Multiply by 2")
    check(result2, expected=np.array([[2, 4], [6, 8], [10, 12]]))

    print("\nTask 3: Add row to each row")
    check(result3, expected=np.array([[11, 22, 33], [14, 25, 36], [17, 28, 39]]),
          hint="matrix + row_to_add broadcasts row to all rows")

    print("\nTask 4: Column means")
    check(column_means, expected=np.array([4., 5., 6.]),
          hint="matrix.mean(axis=0)")

    print("\nTask 4: Centered matrix")
    check(result4, expected=np.array([[-3, -3, -3], [0, 0, 0], [3, 3, 3]]),
          hint="matrix - column_means")
