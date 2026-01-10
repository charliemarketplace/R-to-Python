"""
EXERCISE 9: Exception Handling with try/except

R vs Python:
    R:      tryCatch(expr, error = function(e) default)
    Python: try: expr except Exception: default

Python uses try/except blocks for error handling.

Basic syntax:
    try:
        risky_operation()
    except SomeError:
        handle_error()

With multiple exception types:
    try:
        x = int(user_input)
    except ValueError:
        print("Not a valid integer")
    except TypeError:
        print("Wrong type")

Getting the error message:
    except ValueError as e:
        print(f"Error: {e}")

TASK:
Write a function `safe_divide(a, b)` that:
- Returns a / b if successful
- Returns None if there's a ZeroDivisionError
- Returns None if there's a TypeError (e.g., dividing strings)
"""


# ---- YOUR CODE HERE ----
def safe_divide(a, b):
    """Safely divide a by b, returning None on error."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Test 1: Normal division 10/2")
    check(safe_divide(10, 2), expected=5.0)

    print("\nTest 2: Division by zero 5/0")
    check(safe_divide(5, 0), expected=None,
          hint="Catch ZeroDivisionError and return None")

    print("\nTest 3: Invalid types 'a'/2")
    check(safe_divide('a', 2), expected=None,
          hint="Catch TypeError and return None")

    print("\nTest 4: Float division 7/2")
    check(safe_divide(7, 2), expected=3.5)
