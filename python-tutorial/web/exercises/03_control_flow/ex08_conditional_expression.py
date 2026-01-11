"""
EXERCISE 8: Conditional Expressions (Ternary Operator)

R vs Python:
    R:      ifelse(condition, yes, no)
            # or: if(cond) x else y (for scalars)
    Python: x if condition else y

Python's ternary operator puts the condition in the MIDDLE.
This reads like English: "x if condition is true, else y"

Examples:
    status = "adult" if age >= 18 else "minor"
    sign = "positive" if x > 0 else "non-positive"

Can be used in comprehensions too:
    labels = ["even" if x % 2 == 0 else "odd" for x in range(5)]

TASK A: Set `category` to "high" if score >= 80, else "low"
TASK B: Create a list that labels each number as "even" or "odd"
        For [1, 2, 3, 4, 5] -> ["odd", "even", "odd", "even", "odd"]
"""

score = 75
numbers = [1, 2, 3, 4, 5]

# ---- YOUR CODE HERE ----
category = None  # "high" if score >= 80 else "low"
labels = None    # ["odd", "even", "odd", "even", "odd"]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: Score category")
    check(category, expected="low",
          hint="value_if_true if condition else value_if_false")

    print("\nTask B: Even/odd labels")
    check(labels, expected=["odd", "even", "odd", "even", "odd"],
          hint='["even" if x % 2 == 0 else "odd" for x in numbers]')
