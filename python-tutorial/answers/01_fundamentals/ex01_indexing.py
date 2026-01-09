"""
EXERCISE 1: Zero-Indexing Basics - SOLUTION
"""

fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# ---- YOUR CODE HERE ----
result = fruits[2]  # Third element at index 2
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(result, expected='cherry',
          hint="In Python, the third element is at index 2 (0, 1, 2)")
