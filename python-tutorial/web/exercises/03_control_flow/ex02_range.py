"""
EXERCISE 2: The range() Function

R vs Python:
    R:      1:5      gives c(1, 2, 3, 4, 5)       # Inclusive
    Python: range(5) gives 0, 1, 2, 3, 4         # Exclusive, starts at 0!

range(stop)           - 0 to stop-1
range(start, stop)    - start to stop-1
range(start, stop, step) - with custom step

Key differences from R's seq():
- range() starts at 0 by default (not 1!)
- range() excludes the stop value (like slice notation)
- range() returns an iterator, not a list (use list() to convert)

TASK A: Create a list of numbers from 0 to 9 (inclusive)
TASK B: Create a list of numbers from 1 to 10 (inclusive) - like R's 1:10
TASK C: Create a list of even numbers from 2 to 20 (inclusive)
"""

# ---- YOUR CODE HERE ----
result_a = None  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result_b = None  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_c = None  # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: 0 to 9")
    check(result_a, expected=list(range(10)),
          hint="range(10) gives 0-9, wrap in list()")

    print("\nTask B: 1 to 10 (R-style)")
    check(result_b, expected=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          hint="range(1, 11) - start at 1, stop BEFORE 11")

    print("\nTask C: Even numbers 2 to 20")
    check(result_c, expected=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
          hint="range(start, stop, step) - use step=2")
