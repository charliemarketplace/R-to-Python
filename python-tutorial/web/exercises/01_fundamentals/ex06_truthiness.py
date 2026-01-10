"""
EXERCISE 6: Truthiness (Falsy Values)

R vs Python:
    R:      if(length(x) > 0) - must explicitly check
    Python: if x: - empty collections are "falsy"

In Python, these values are "falsy" (evaluate to False in boolean context):
    - False
    - None
    - 0, 0.0
    - "" (empty string)
    - [] (empty list)
    - {} (empty dict)
    - set() (empty set)

Everything else is "truthy"!

TASK:
For each value below, predict whether it's truthy or falsy.
Set each result to True if the value is truthy, False if falsy.
"""

# Values to evaluate
val1 = []           # empty list
val2 = [0]          # list with one element (zero)
val3 = ""           # empty string
val4 = "False"      # string containing "False"
val5 = 0            # integer zero
val6 = None         # None
val7 = {}           # empty dict
val8 = {"a": None}  # dict with None value

# ---- YOUR CODE HERE ----
# Set each to True if truthy, False if falsy
result1 = None  # Is [] truthy?
result2 = None  # Is [0] truthy?
result3 = None  # Is "" truthy?
result4 = None  # Is "False" truthy?
result5 = None  # Is 0 truthy?
result6 = None  # Is None truthy?
result7 = None  # Is {} truthy?
result8 = None  # Is {"a": None} truthy?
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("1. Empty list []")
    check(result1, expected=False, hint="Empty collections are falsy")

    print("\n2. List with zero [0]")
    check(result2, expected=True, hint="Non-empty collections are truthy, even if they contain falsy values")

    print("\n3. Empty string ''")
    check(result3, expected=False, hint="Empty string is falsy")

    print("\n4. String 'False'")
    check(result4, expected=True, hint="Non-empty strings are truthy, even if they say 'False'!")

    print("\n5. Integer 0")
    check(result5, expected=False, hint="Zero is falsy")

    print("\n6. None")
    check(result6, expected=False, hint="None is falsy")

    print("\n7. Empty dict {}")
    check(result7, expected=False, hint="Empty collections are falsy")

    print("\n8. Dict with None value {'a': None}")
    check(result8, expected=True, hint="Non-empty dict is truthy, even if values are None")
