"""
EXERCISE 1: For Loops - Iterating Over Objects

R vs Python:
    R:      for(i in 1:length(x)) { print(x[i]) }  # Index-based
    Python: for item in x: print(item)             # Direct iteration

Python's for loop iterates DIRECTLY over elements, not indices!
This is more readable and less error-prone.

R habit to AVOID:
    for i in range(len(lst)):  # Works but unpythonic
        print(lst[i])

Pythonic way:
    for item in lst:  # Direct iteration
        print(item)

TASK:
Given the list of temperatures in Fahrenheit, create a new list with
temperatures converted to Celsius using a for loop.
Formula: C = (F - 32) * 5/9
"""

fahrenheit = [32, 68, 77, 98.6, 212]

# ---- YOUR CODE HERE ----
celsius = []  # Build this list using a for loop

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    expected = [0.0, 20.0, 25.0, 37.0, 100.0]
    check(celsius, expected=expected, rtol=0.01,
          hint="Loop: for f in fahrenheit: ... append (f - 32) * 5/9")
