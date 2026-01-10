"""
EXERCISE 2: Negative Indexing

R vs Python:
    R:      x[length(x)] gets the LAST element
            x[-1] REMOVES the first element (returns rest)
    Python: x[-1] gets the LAST element
            x[-2] gets the SECOND-TO-LAST element

In Python, negative indices count from the end. This is convenient!
WARNING: In R, negative indices mean "exclude". In Python, they mean "from end".

TASK:
Given the list `numbers`, return the SECOND-TO-LAST element using negative indexing.
"""

numbers = [10, 20, 30, 40, 50, 60, 70]

# ---- YOUR CODE HERE ----
result = None  # Replace with your answer (should be 60)
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(result, expected=60,
          hint="x[-1] is last, x[-2] is second-to-last")
