"""
EXERCISE 10: The Late Binding Closure Trap

This is a SUBTLE Python gotcha that has bitten many developers!

When you create functions (especially lambdas) in a loop that reference
the loop variable, all functions will reference the FINAL value of
that variable, not the value when the function was created.

THE BUG:
    funcs = [lambda: x for x in range(5)]
    [f() for f in funcs]  # Returns [4, 4, 4, 4, 4] - all 4!

WHY: The lambda references `x`, but `x` is looked up when the
lambda is CALLED, not when it's CREATED. By call time, x is 4.

THE FIX - capture the value as a default argument:
    funcs = [lambda x=x: x for x in range(5)]  # x=x captures current x
    [f() for f in funcs]  # Returns [0, 1, 2, 3, 4] - correct!

TASK:
Fix the `make_multipliers` function so that each returned function
multiplies by its correct factor.
Currently: make_multipliers() returns functions that all multiply by 4
Should: make_multipliers() returns functions that multiply by 0, 1, 2, 3, 4
"""


# ---- YOUR CODE HERE ----
def make_multipliers():
    """Return a list of 5 functions that multiply by 0, 1, 2, 3, 4."""
    # BUG: All lambdas will use the final value of i (which is 4)
    return [lambda x: x * i for i in range(5)]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    multipliers = make_multipliers()

    print("Testing multipliers[0](10) - should multiply by 0")
    check(multipliers[0](10), expected=0,
          hint="Use default argument: lambda x, i=i: x * i")

    print("\nTesting multipliers[1](10) - should multiply by 1")
    check(multipliers[1](10), expected=10)

    print("\nTesting multipliers[2](10) - should multiply by 2")
    check(multipliers[2](10), expected=20)

    print("\nTesting multipliers[3](10) - should multiply by 3")
    check(multipliers[3](10), expected=30)

    print("\nTesting multipliers[4](10) - should multiply by 4")
    check(multipliers[4](10), expected=40)
