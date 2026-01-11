"""
EXERCISE 7: Variable Scope (LEGB Rule)

Python's scope resolution order: LEGB
- Local: Inside the current function
- Enclosing: Inside enclosing functions (closures)
- Global: Module level
- Built-in: Python's built-in names

R vs Python:
    R:      Uses lexical scoping, searches up through environments
    Python: LEGB rule, with explicit `global` and `nonlocal` keywords

THE TRAP (UnboundLocalError):
    x = 10
    def foo():
        print(x)  # ERROR! Python sees assignment below, marks x as local
        x = 20    # This makes x local to the entire function

    # Fix with global (if you really need it):
    def foo():
        global x
        print(x)
        x = 20

    # Or better, don't modify globals:
    def foo():
        print(x)  # This works - just reading global x

TASK:
The function `counter` has a bug. It's supposed to count how many times
it's been called, but it crashes. Fix it using the `global` keyword.

Note: In real code, prefer class-based or closure-based solutions over
global variables. This exercise demonstrates the concept.
"""

call_count = 0


# ---- YOUR CODE HERE ----
def counter():
    """Increment call_count and return the new value."""
    # BUG: This will raise UnboundLocalError
    call_count = call_count + 1  # Fix this line!
    return call_count
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    # Reset for testing
    call_count = 0

    print("Test 1: First call")
    check(counter(), expected=1,
          hint="Use 'global call_count' at the start of the function")

    print("\nTest 2: Second call")
    check(counter(), expected=2)

    print("\nTest 3: Third call")
    check(counter(), expected=3)
