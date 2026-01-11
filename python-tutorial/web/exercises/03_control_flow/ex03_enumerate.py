"""
EXERCISE 3: enumerate() - When You Need Both Index AND Value

R vs Python:
    R:      for(i in seq_along(x)) { cat(i, x[i]) }
    Python: for i, val in enumerate(x): print(i, val)

enumerate() gives you (index, value) pairs - perfect when you need both!

Without enumerate (unpythonic):
    for i in range(len(fruits)):
        print(i, fruits[i])

With enumerate (Pythonic):
    for i, fruit in enumerate(fruits):
        print(i, fruit)

You can also start at a different index:
    for i, fruit in enumerate(fruits, start=1):  # 1-based like R!

TASK:
Create a dictionary mapping each fruit to its position (1-based, like R indexing).
Result should be: {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
"""

fruits = ['apple', 'banana', 'cherry', 'date']

# ---- YOUR CODE HERE ----
fruit_positions = {}  # Build this dict using enumerate

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    expected = {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}
    check(fruit_positions, expected=expected,
          hint="Use enumerate(fruits, start=1) to get 1-based indices")
