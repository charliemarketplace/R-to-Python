"""
EXERCISE 5: Reference vs Copy (The Big Gotcha!)

R vs Python:
    R:      y <- x creates a COPY (copy-on-modify semantics)
    Python: y = x creates a REFERENCE (same object!)

This is one of the BIGGEST differences and source of bugs for R users.

In Python:
    y = x           # y points to SAME object as x
    y = x.copy()    # y is a NEW object (shallow copy)
    y = x[:]        # also creates a shallow copy (for lists)

TASK:
The code below has a bug. `original` is being modified when we only
wanted to modify `modified`. Fix it by making `modified` a proper copy.
"""

original = [1, 2, 3, 4, 5]

# ---- YOUR CODE HERE ----
# Fix this line so that modifying `modified` doesn't change `original`
modified = original  # BUG: This creates a reference, not a copy!
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
