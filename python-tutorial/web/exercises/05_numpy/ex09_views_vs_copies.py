"""
EXERCISE 9: Views vs Copies - A Major Gotcha!

THE TRAP:
    arr = np.array([1, 2, 3, 4, 5])
    slice_view = arr[1:4]
    slice_view[0] = 99
    print(arr)  # [1, 99, 3, 4, 5] - Original modified!

NumPy slices return VIEWS, not copies!
This is for performance but can cause bugs.

Views (share memory with original):
    arr[1:4]          # Slice
    arr.reshape(...)  # Reshape
    arr.T             # Transpose

Copies (independent):
    arr.copy()        # Explicit copy
    arr[[1, 2, 3]]    # Fancy indexing (with list/array of indices)
    arr[arr > 0]      # Boolean indexing

How to check:
    np.shares_memory(a, b)  # True if they share memory

R comparison:
    R typically copies on modification (copy-on-modify semantics)
    NumPy views are more like R's data.table behavior

TASK:
1. Create a slice view and show it shares memory
2. Create an independent copy
3. Demonstrate fancy indexing creates a copy
"""
import numpy as np

original = np.array([10, 20, 30, 40, 50])

# ---- YOUR CODE HERE ----
# Task 1: Create a slice (view) of elements 1-3
view_slice = None
# Check: np.shares_memory(original, view_slice) should be True

# Task 2: Create an independent copy of elements 1-3
independent_copy = None
# Check: np.shares_memory(original, independent_copy) should be False

# Task 3: Use fancy indexing to get elements at indices [1, 3]
fancy = None
# Check: np.shares_memory(original, fancy) should be False
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Slice view")
    check(view_slice is not None and np.array_equal(view_slice, np.array([20, 30, 40])),
          expected=True, hint="original[1:4]")
    print("Shares memory:", np.shares_memory(original, view_slice))
    check(np.shares_memory(original, view_slice), expected=True,
          hint="Slices are views - they share memory")

    print("\nTask 2: Independent copy")
    check(independent_copy is not None and np.array_equal(independent_copy, np.array([20, 30, 40])),
          expected=True, hint="original[1:4].copy()")
    check(np.shares_memory(original, independent_copy), expected=False,
          hint="Use .copy() to create independent copy")

    print("\nTask 3: Fancy indexing")
    check(fancy is not None and np.array_equal(fancy, np.array([20, 40])),
          expected=True, hint="original[[1, 3]]")
    check(np.shares_memory(original, fancy), expected=False,
          hint="Fancy indexing creates a copy, not a view")
