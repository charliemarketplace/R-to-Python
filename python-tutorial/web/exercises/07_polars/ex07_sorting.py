"""
EXERCISE 7: Sorting in Polars

pandas vs Polars:
    pandas: df.sort_values("col", ascending=False)
    Polars: df.sort("col", descending=True)

Polars sorting:

    df.sort("col")                          # Ascending
    df.sort("col", descending=True)         # Descending
    df.sort(["a", "b"])                     # Multiple columns
    df.sort(["a", "b"], descending=[True, False])  # Mixed

Note: Polars uses `descending` not `ascending` (opposite default!)

Sorting with expressions:
    df.sort(pl.col("name").str.len())  # Sort by string length

TASK:
Given the students DataFrame:
1. Sort by score ascending
2. Sort by score descending
3. Sort by grade ascending, then score descending
"""
import polars as pl

students = pl.DataFrame({
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
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: By score ascending")
    check(by_score_asc["name"].to_list(), expected=["Dave", "Bob", "Eve", "Alice", "Carol"],
          hint='df.sort("score")')

    print("\nTask 2: By score descending")
    check(by_score_desc["name"].to_list(), expected=["Carol", "Alice", "Eve", "Bob", "Dave"],
          hint='df.sort("score", descending=True)')

    print("\nTask 3: By grade asc, score desc")
    check(by_grade_then_score["name"].to_list(), expected=["Carol", "Alice", "Eve", "Bob", "Dave"],
          hint='df.sort(["grade", "score"], descending=[False, True])')
