"""
EXERCISE 6: **kwargs - Variable Keyword Arguments

R vs Python:
    R:      function(...) { list(...) }  # mixed positional/named
    Python: def func(**kwargs): ...       # only keyword args

**kwargs collects extra KEYWORD arguments into a dictionary.
The double asterisk (**) means "pack remaining keyword args here".

    def print_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_info(name="Alice", age=30, city="NYC")
    # kwargs = {'name': 'Alice', 'age': 30, 'city': 'NYC'}

Combining *args and **kwargs:
    def func(*args, **kwargs):
        print(f"Positional: {args}")
        print(f"Keyword: {kwargs}")

    func(1, 2, 3, x=10, y=20)
    # args = (1, 2, 3)
    # kwargs = {'x': 10, 'y': 20}

TASK:
Write a function `build_profile(name, **attributes)` that:
- Takes a required name parameter
- Takes any number of keyword arguments for attributes
- Returns a dictionary with 'name' plus all the attributes
"""


# ---- YOUR CODE HERE ----
def build_profile(name, **attributes):
    """Build a profile dict with name and any additional attributes."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Test 1: Basic profile")
    check(build_profile("Alice", age=30, city="NYC"),
          expected={'name': 'Alice', 'age': 30, 'city': 'NYC'})

    print("\nTest 2: Name only")
    check(build_profile("Bob"),
          expected={'name': 'Bob'},
          hint="Should work with just the name, no extra attributes")

    print("\nTest 3: Many attributes")
    check(build_profile("Carol", job="engineer", level="senior", remote=True),
          expected={'name': 'Carol', 'job': 'engineer', 'level': 'senior', 'remote': True})
