"""
EXERCISE 5: *args - Variable Positional Arguments

R vs Python:
    R:      function(...) { list(...) }  # dot-dot-dot
    Python: def func(*args): return args  # *args is a tuple

*args collects extra positional arguments into a tuple.
The asterisk (*) means "pack remaining positional args here".

    def sum_all(*numbers):
        return sum(numbers)

    sum_all(1, 2, 3)       # numbers = (1, 2, 3), returns 6
    sum_all(1, 2, 3, 4, 5) # numbers = (1, 2, 3, 4, 5), returns 15

You can have regular parameters before *args:
    def greet(greeting, *names):
        for name in names:
            print(f"{greeting}, {name}!")

    greet("Hello", "Alice", "Bob", "Carol")

TASK:
Write a function `product(*numbers)` that:
- Takes any number of numeric arguments
- Returns their product (all multiplied together)
- Returns 1 if no arguments are given (empty product)
"""


# ---- YOUR CODE HERE ----
def product(*numbers):
    """Return the product of all arguments (1 if none given)."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Test 1: product(2, 3, 4)")
    check(product(2, 3, 4), expected=24)

    print("\nTest 2: product(5)")
    check(product(5), expected=5)

    print("\nTest 3: product() - no arguments")
    check(product(), expected=1,
          hint="Empty product is 1 (like sum of nothing is 0)")

    print("\nTest 4: product(1, 2, 3, 4, 5)")
    check(product(1, 2, 3, 4, 5), expected=120)
