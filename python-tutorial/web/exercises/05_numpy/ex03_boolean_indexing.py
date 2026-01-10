"""
EXERCISE 3: Boolean Indexing

R vs Python:
    R:      x[x > 5]           # Elements greater than 5
    Python: arr[arr > 5]       # Same syntax!

Boolean indexing works the same way:
1. Create a boolean mask: arr > 5 creates array of True/False
2. Use mask to select: arr[mask] returns matching elements

    arr = np.array([1, 5, 3, 8, 2, 9])
    mask = arr > 4    # [False, True, False, True, False, True]
    arr[mask]         # [5, 8, 9]

Compound conditions (different from R!):
    R:      x[x > 2 & x < 8]
    Python: arr[(arr > 2) & (arr < 8)]  # Parentheses required!

    & = and (element-wise)
    | = or (element-wise)
    ~ = not (element-wise)

TASK:
Given the array of test scores:
1. Select all scores above 80
2. Select scores between 70 and 90 (inclusive)
3. Count how many scores are below 60
4. Replace all scores below 60 with 60 (floor at 60)
"""
import numpy as np

scores = np.array([85, 55, 90, 70, 45, 88, 72, 60, 95, 58])

# ---- YOUR CODE HERE ----
# Task 1: Scores above 80
above_80 = None

# Task 2: Scores between 70 and 90 (inclusive)
in_range = None

# Task 3: Count of scores below 60
count_below_60 = None

# Task 4: Replace scores below 60 with 60
# Make a copy first to avoid modifying original
floored_scores = scores.copy()
# Your code to floor at 60...

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Scores above 80")
    check(above_80, expected=np.array([85, 90, 88, 95]),
          hint="scores[scores > 80]")

    print("\nTask 2: Scores 70-90 inclusive")
    check(in_range, expected=np.array([85, 90, 70, 88, 72]),
          hint="scores[(scores >= 70) & (scores <= 90)] - need parentheses!")

    print("\nTask 3: Count below 60")
    check(count_below_60, expected=3,
          hint="(scores < 60).sum() or len(scores[scores < 60])")

    print("\nTask 4: Floored scores")
    check(floored_scores, expected=np.array([85, 60, 90, 70, 60, 88, 72, 60, 95, 60]),
          hint="floored_scores[floored_scores < 60] = 60")
