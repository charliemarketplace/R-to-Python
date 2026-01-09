"""
EXERCISE 3: Boolean Indexing - SOLUTION
"""
import numpy as np

scores = np.array([85, 55, 90, 70, 45, 88, 72, 60, 95, 58])

# ---- YOUR CODE HERE ----
# Task 1: Scores above 80
above_80 = scores[scores > 80]

# Task 2: Scores between 70 and 90 (inclusive)
in_range = scores[(scores >= 70) & (scores <= 90)]

# Task 3: Count of scores below 60
count_below_60 = (scores < 60).sum()

# Task 4: Replace scores below 60 with 60
floored_scores = scores.copy()
floored_scores[floored_scores < 60] = 60
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
