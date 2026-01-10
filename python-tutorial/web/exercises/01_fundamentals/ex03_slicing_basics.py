"""
EXERCISE 3: Slice Notation Basics

R vs Python:
    R:      x[2:4] gets elements 2, 3, and 4 (inclusive on both ends)
    Python: x[1:4] gets elements at index 1, 2, 3 (EXCLUSIVE of end)

Python slice syntax: x[start:stop]
- start: index to begin (inclusive)
- stop: index to end (EXCLUSIVE - this is the tricky part!)

So x[1:4] returns elements at indices 1, 2, 3 (NOT 4!)

TASK:
Given the list `letters`, extract ['c', 'd', 'e'] using slice notation.
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# ---- YOUR CODE HERE ----
result = None  # Replace with your slice
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(result, expected=['c', 'd', 'e'],
          hint="'c' is at index 2. To include 'e' (index 4), stop must be 5")
