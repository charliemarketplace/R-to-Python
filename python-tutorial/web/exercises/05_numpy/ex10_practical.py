"""
EXERCISE 10: Practical NumPy - Putting It Together

A real-world-ish exercise combining multiple NumPy concepts.

SCENARIO:
You have exam scores for 5 students across 4 subjects.
Perform common data analysis operations.

This combines:
- Array creation
- Indexing and slicing
- Boolean operations
- Aggregations with axis
- Broadcasting
"""
import numpy as np

# Rows = students, Columns = subjects (Math, Science, English, History)
scores = np.array([
    [85, 90, 78, 92],   # Student 0
    [76, 88, 95, 70],   # Student 1
    [90, 72, 85, 88],   # Student 2
    [65, 80, 70, 75],   # Student 3
    [95, 95, 92, 98],   # Student 4
])

subject_names = ['Math', 'Science', 'English', 'History']

# ---- YOUR CODE HERE ----
# Task 1: Calculate each student's average score (mean across subjects)
student_averages = None  # Shape (5,)

# Task 2: Calculate each subject's average (mean across students)
subject_averages = None  # Shape (4,)

# Task 3: Find the highest score in each subject
highest_per_subject = None  # Shape (4,)

# Task 4: Which student has the highest overall average?
# (Return the student index, 0-based)
top_student_idx = None  # Single integer

# Task 5: How many scores are below 75?
count_below_75 = None  # Single integer

# Task 6: Curve the scores: add 5 points to everyone's Math score (column 0)
# Make a copy first!
curved_scores = scores.copy()
# Modify curved_scores column 0...

# Task 7: Normalize each subject to mean=0, std=1 (z-score by column)
# Each column should have mean ~0 and std ~1
normalized = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Student averages")
    check(student_averages, expected=scores.mean(axis=1), rtol=0.01)

    print("\nTask 2: Subject averages")
    check(subject_averages, expected=scores.mean(axis=0), rtol=0.01)

    print("\nTask 3: Highest per subject")
    check(highest_per_subject, expected=np.array([95, 95, 95, 98]))

    print("\nTask 4: Top student index")
    check(top_student_idx, expected=4,
          hint="student_averages.argmax()")

    print("\nTask 5: Count below 75")
    check(count_below_75, expected=4,
          hint="(scores < 75).sum()")

    print("\nTask 6: Curved Math scores")
    expected_math = np.array([90, 81, 95, 70, 100])
    check(curved_scores[:, 0], expected=expected_math,
          hint="curved_scores[:, 0] += 5 or curved_scores[:, 0] = curved_scores[:, 0] + 5")

    print("\nTask 7: Normalized columns have mean ~0")
    if normalized is not None:
        col_means = normalized.mean(axis=0)
        check(np.allclose(col_means, 0, atol=1e-10), expected=True,
              hint="normalized = (scores - scores.mean(axis=0)) / scores.std(axis=0)")
