"""
EXERCISE 5: While Loops

R vs Python:
    R:      while(condition) { ... }
    Python: while condition: ...

While loops are similar in both languages. They're less common in data science
(prefer vectorized operations), but useful for:
- Reading until end of file
- Iterating until convergence
- User input loops

Key difference: Python uses `True`/`False` (capitalized), R uses `TRUE`/`FALSE`.

TASK:
Use a while loop to calculate the sum of numbers from 1 to 100 (inclusive).
This is the classic Gauss sum: 1 + 2 + 3 + ... + 100 = 5050
"""

# ---- YOUR CODE HERE ----
total = 0
# Use a while loop to add numbers 1 through 100 to total

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    check(total, expected=5050,
          hint="Initialize counter at 1, loop while counter <= 100, add counter to total, increment counter")
