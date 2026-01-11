"""
EXERCISE 1: Basic Function Definition

R vs Python:
    R:      my_func <- function(x, y) { x + y }
    Python: def my_func(x, y): return x + y

Key differences:
- Python uses `def` keyword, not `<- function()`
- Python uses `return` (optional in R)
- Python uses indentation for the body (no braces!)
- If you don't return, Python returns None (R returns last expression)

IMPORTANT: Python requires explicit `return`!
    def add(x, y):
        x + y  # BUG: This computes but doesn't return!

    def add(x, y):
        return x + y  # Correct!

TASK:
Write a function `circle_area(radius)` that returns the area of a circle.
Formula: area = pi * radius^2
Use 3.14159 for pi (or import math and use math.pi)
"""


# ---- YOUR CODE HERE ----
def circle_area(radius):
    """Calculate the area of a circle given its radius."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Test 1: circle_area(1)")
    check(circle_area(1), expected=3.14159, rtol=0.001)

    print("\nTest 2: circle_area(2)")
    check(circle_area(2), expected=12.56636, rtol=0.001)

    print("\nTest 3: circle_area(0)")
    check(circle_area(0), expected=0.0)
