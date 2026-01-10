"""
EXERCISE 1: NumPy Array Creation

R vs Python:
    R:      c(1, 2, 3)            # Vector
            matrix(1:9, nrow=3)    # Matrix
            seq(0, 10, by=2)       # Sequence
    Python: np.array([1, 2, 3])
            np.arange(9).reshape(3, 3)
            np.arange(0, 11, 2)

Common array creation functions:
    np.array([1, 2, 3])      # From Python list
    np.zeros(5)              # [0, 0, 0, 0, 0]
    np.ones((2, 3))          # 2x3 array of ones
    np.arange(start, stop, step)  # Like range() but returns array
    np.linspace(start, stop, num) # num evenly spaced values

Key difference from R:
- NumPy arrays are homogeneous (one dtype)
- Shape is explicit: (rows, cols) tuple
- arange stop is EXCLUSIVE (like Python range)

TASK:
Create the following arrays:
1. A 1D array [1, 2, 3, 4, 5]
2. A 2x3 array of zeros
3. Numbers from 0 to 9 (inclusive) using arange
4. 5 evenly spaced numbers from 0 to 1 using linspace
"""
import numpy as np

# ---- YOUR CODE HERE ----
arr1 = None  # [1, 2, 3, 4, 5]
arr2 = None  # 2x3 zeros
arr3 = None  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr4 = None  # [0.0, 0.25, 0.5, 0.75, 1.0]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: 1D array [1,2,3,4,5]")
    check(arr1, expected=np.array([1, 2, 3, 4, 5]))

    print("\nTask 2: 2x3 zeros")
    check(arr2, expected=np.zeros((2, 3)),
          hint="np.zeros((2, 3)) - note the tuple for shape")

    print("\nTask 3: 0 to 9 with arange")
    check(arr3, expected=np.arange(10),
          hint="np.arange(10) gives 0-9 (stop is exclusive)")

    print("\nTask 4: linspace 0 to 1")
    check(arr4, expected=np.linspace(0, 1, 5),
          hint="np.linspace(0, 1, 5) gives 5 points from 0 to 1")
