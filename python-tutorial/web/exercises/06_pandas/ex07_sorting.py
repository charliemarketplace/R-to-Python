"""
EXERCISE 7: Sorting DataFrames

R vs Python:
    R:      arrange(df, col)
            arrange(df, desc(col))
    Python: df.sort_values("col")
            df.sort_values("col", ascending=False)

Sorting methods:
    df.sort_values("col")                    # Single column
    df.sort_values("col", ascending=False)   # Descending
    df.sort_values(["a", "b"])              # Multiple columns
    df.sort_values(["a", "b"], ascending=[True, False])  # Mixed

    df.sort_index()                          # Sort by index

Note: sort_values() returns a NEW DataFrame by default.
Use inplace=True to modify in place (but not recommended).

After sorting, index is preserved (not reset):
    df_sorted = df.sort_values("x")
    df_sorted.reset_index(drop=True)  # Reset to 0, 1, 2, ...

TASK:
Given the students DataFrame:
1. Sort by score ascending
2. Sort by score descending
3. Sort by grade (ascending), then by score (descending)
4. Sort by score and reset index to 0, 1, 2, ...
"""
import pandas as pd

students = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "grade": ["A", "B", "A", "C", "B"],
    "score": [92, 85, 95, 72, 88]
})

# ---- YOUR CODE HERE ----
# Task 1: Sort by score ascending
by_score_asc = None

# Task 2: Sort by score descending
by_score_desc = None

# Task 3: Sort by grade asc, then score desc
by_grade_then_score = None

# Task 4: Sort by score asc and reset index
sorted_reset = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: By score ascending")
    check(list(by_score_asc["name"]), expected=["Dave", "Bob", "Eve", "Alice", "Carol"],
          hint='df.sort_values("score")')

    print("\nTask 2: By score descending")
    check(list(by_score_desc["name"]), expected=["Carol", "Alice", "Eve", "Bob", "Dave"],
          hint='df.sort_values("score", ascending=False)')

    print("\nTask 3: By grade asc, score desc")
    check(list(by_grade_then_score["name"]), expected=["Carol", "Alice", "Eve", "Bob", "Dave"],
          hint='df.sort_values(["grade", "score"], ascending=[True, False])')

    print("\nTask 4: Sorted and reset index")
    check(list(sorted_reset.index), expected=[0, 1, 2, 3, 4],
          hint='df.sort_values("score").reset_index(drop=True)')
