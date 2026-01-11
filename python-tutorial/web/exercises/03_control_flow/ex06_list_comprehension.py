"""
EXERCISE 6: List Comprehensions

R vs Python:
    R:      sapply(x, function(i) i^2)
            # or: x^2 (vectorized)
    Python: [i**2 for i in x]  # List comprehension

List comprehensions are a Pythonic way to create lists from iterables.
They're more concise than for loops for simple transformations.

Syntax: [expression for item in iterable]
         [expression for item in iterable if condition]

Examples:
    squares = [x**2 for x in range(10)]         # [0, 1, 4, 9, ...]
    evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]

TASK A: Create a list of squares from 1 to 10: [1, 4, 9, 16, ..., 100]
TASK B: Create a list of only the even numbers from 1-20: [2, 4, 6, ..., 20]
TASK C: Create a list of squares of even numbers from 1-10: [4, 16, 36, 64, 100]
"""

# ---- YOUR CODE HERE ----
squares = None       # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evens = None         # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
even_squares = None  # [4, 16, 36, 64, 100]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: Squares 1-10")
    check(squares, expected=[1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
          hint="[x**2 for x in range(1, 11)]")

    print("\nTask B: Even numbers 1-20")
    check(evens, expected=[2, 4, 6, 8, 10, 12, 14, 16, 18, 20],
          hint="[x for x in range(1, 21) if x % 2 == 0]")

    print("\nTask C: Squares of even numbers 1-10")
    check(even_squares, expected=[4, 16, 36, 64, 100],
          hint="Combine: [x**2 for x in range(...) if x % 2 == 0]")
