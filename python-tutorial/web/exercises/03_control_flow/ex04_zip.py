"""
EXERCISE 4: zip() - Parallel Iteration

R vs Python:
    R:      mapply(function(a, b) a + b, x, y)
            # or: for(i in seq_along(x)) { x[i] + y[i] }
    Python: for a, b in zip(x, y): a + b

zip() combines multiple iterables element-by-element.
It stops at the shortest iterable (no recycling like R!).

    names = ['Alice', 'Bob', 'Carol']
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age}")

WARNING: Unlike R, Python does NOT recycle! zip stops at shortest.

TASK:
Given two lists of names and scores, create a dictionary mapping names to scores.
Result: {'Alice': 85, 'Bob': 92, 'Carol': 78, 'Dave': 95}
"""

names = ['Alice', 'Bob', 'Carol', 'Dave']
scores = [85, 92, 78, 95]

# ---- YOUR CODE HERE ----
gradebook = {}  # Build this dict using zip

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    expected = {'Alice': 85, 'Bob': 92, 'Carol': 78, 'Dave': 95}
    check(gradebook, expected=expected,
          hint="for name, score in zip(names, scores): ... OR use dict(zip(names, scores))")
