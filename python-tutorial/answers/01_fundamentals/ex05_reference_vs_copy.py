"""
EXERCISE 5: Reference vs Copy - SOLUTION
"""

original = [1, 2, 3, 4, 5]

# ---- YOUR CODE HERE ----
modified = original.copy()  # FIX: Use .copy() to create independent copy
# ---- END YOUR CODE ----

# This modification should NOT affect `original`
modified.append(6)
modified[0] = 999

# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    print("Checking that original is unchanged:")
    check(original, expected=[1, 2, 3, 4, 5],
          hint="Use .copy() or [:] to create an independent copy")
    print("\nChecking that modified has the changes:")
    check(modified, expected=[999, 2, 3, 4, 5, 6])
