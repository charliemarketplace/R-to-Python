"""
EXERCISE 1: Zero-Indexing Basics

R vs Python:
    R:      x[1] gets the FIRST element
    Python: x[0] gets the FIRST element

In R, indexing starts at 1. In Python, indexing starts at 0.
This is one of the most common sources of off-by-one errors for R users.

TASK:
Given the list `fruits`, return the THIRD element (which is 'cherry').
"""

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# ---- YOUR CODE HERE ----
result = None  # Replace with your answer
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(result, expected='cherry',
          hint="In Python, the third element is at index 2 (0, 1, 2)")
