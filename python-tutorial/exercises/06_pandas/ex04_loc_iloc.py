"""
EXERCISE 4: loc vs iloc - Label vs Integer Location

R vs Python:
    R:      df[1, 2]        # Row 1, column 2 (1-indexed)
    Python: df.iloc[0, 1]   # Row 0, column 1 (0-indexed integer)
            df.loc[0, "col"] # Row with INDEX 0, column "col"

The two accessors:
    .loc[row_labels, col_labels]  - Label-based (like R's row.names)
    .iloc[row_ints, col_ints]     - Integer position (like R's numeric indexing)

CRITICAL: The index is NOT always 0, 1, 2...!
    df_filtered = df[df["x"] > 5]  # Index might be [2, 5, 7]
    df_filtered.iloc[0]  # First row (index 2)
    df_filtered.loc[0]   # ERROR! No row with index label 0

When to use which:
    .iloc - You want the nth row regardless of index
    .loc  - You want a specific labeled row/column

Slicing:
    df.loc["a":"c"]    # Inclusive of "c"!
    df.iloc[0:3]       # Exclusive of 3 (Python-style)

TASK:
Given the DataFrame with custom index:
1. Get the first row using iloc
2. Get the row with index label 'b' using loc
3. Get rows 'a' through 'c' using loc
4. Get the first 2 rows using iloc
"""
import pandas as pd

df = pd.DataFrame({
    "x": [10, 20, 30, 40, 50],
    "y": [1, 2, 3, 4, 5]
}, index=["a", "b", "c", "d", "e"])

# ---- YOUR CODE HERE ----
# Task 1: First row (as Series)
first_row = None

# Task 2: Row with index 'b' (as Series)
row_b = None

# Task 3: Rows 'a' through 'c' (as DataFrame) - note: loc is INCLUSIVE
rows_a_to_c = None

# Task 4: First 2 rows (as DataFrame)
first_two = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: First row (iloc)")
    check(dict(first_row), expected={"x": 10, "y": 1},
          hint="df.iloc[0]")

    print("\nTask 2: Row 'b' (loc)")
    check(dict(row_b), expected={"x": 20, "y": 2},
          hint='df.loc["b"]')

    print("\nTask 3: Rows 'a' to 'c' (loc)")
    check(list(rows_a_to_c.index), expected=["a", "b", "c"],
          hint='df.loc["a":"c"] - note: inclusive!')

    print("\nTask 4: First 2 rows (iloc)")
    check(list(first_two.index), expected=["a", "b"],
          hint="df.iloc[0:2] or df.iloc[:2]")
