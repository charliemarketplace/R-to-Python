"""
EXERCISE 2: Positional and Keyword Arguments

R vs Python:
    R:      func(1, 2)  or  func(x=1, y=2)  or  func(y=2, x=1)
    Python: func(1, 2)  or  func(x=1, y=2)  or  func(y=2, x=1)

Both languages support positional and keyword arguments.

BUT Python has a strict rule:
    Positional arguments must come BEFORE keyword arguments!

    func(1, y=2)     # OK: positional, then keyword
    func(x=1, 2)     # ERROR: keyword before positional

In R, you can mix them more freely. Python is stricter.

TASK:
The function `greet` takes three parameters. Call it in three different ways:
1. All positional arguments
2. All keyword arguments (in any order you like)
3. Mix: first positional, rest keyword
"""


def greet(name, greeting, punctuation):
    """Return a greeting message."""
    return f"{greeting}, {name}{punctuation}"


# ---- YOUR CODE HERE ----
# Call greet("Alice", "Hello", "!") in three ways:

# 1. All positional (should produce "Hello, Alice!")
result1 = None

# 2. All keyword, in different order (should produce "Hello, Alice!")
result2 = None

# 3. First positional, rest keyword (should produce "Hello, Alice!")
result3 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    expected = "Hello, Alice!"

    print("Test 1: All positional")
    check(result1, expected=expected,
          hint='greet("Alice", "Hello", "!")')

    print("\nTest 2: All keyword (any order)")
    check(result2, expected=expected,
          hint='greet(punctuation="!", name="Alice", greeting="Hello")')

    print("\nTest 3: Mixed (positional first)")
    check(result3, expected=expected,
          hint='greet("Alice", punctuation="!", greeting="Hello")')
