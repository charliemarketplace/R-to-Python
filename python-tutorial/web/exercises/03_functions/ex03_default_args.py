"""
EXERCISE 3: Default Arguments

R vs Python:
    R:      function(x, y=10) { x + y }
    Python: def func(x, y=10): return x + y

Default arguments work similarly in both languages.

Python rule: Parameters with defaults must come AFTER parameters without!

    def func(a, b=1, c=2):  # OK
    def func(a=1, b, c=2):  # ERROR: non-default after default

This is slightly different from R where you can have:
    function(a=1, b, c=2)  # OK in R (but confusing)

TASK:
Write a function `power(base, exponent=2)` that:
- Takes a base number
- Takes an optional exponent (default 2, i.e., square)
- Returns base raised to the exponent
"""


# ---- YOUR CODE HERE ----
def power(base, exponent=2):
    """Raise base to exponent (default: square)."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Test 1: power(3) - default exponent (square)")
    check(power(3), expected=9,
          hint="3^2 = 9")

    print("\nTest 2: power(2, 3) - explicit exponent (cube)")
    check(power(2, 3), expected=8,
          hint="2^3 = 8")

    print("\nTest 3: power(5, exponent=0) - keyword argument")
    check(power(5, exponent=0), expected=1,
          hint="Anything to the 0 power is 1")

    print("\nTest 4: power(2, 10)")
    check(power(2, 10), expected=1024)
