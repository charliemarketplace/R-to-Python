"""
EXERCISE 1: Polars DataFrame Creation

Polars is a modern, fast alternative to pandas:
- Written in Rust (very fast!)
- No index (cleaner mental model)
- Expression-based API
- Lazy evaluation support

Creating DataFrames:

    import polars as pl

    # From dict (like pandas)
    df = pl.DataFrame({
        "name": ["Alice", "Bob"],
        "age": [30, 25]
    })

    # From list of dicts
    df = pl.DataFrame([
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ])

Key differences from pandas:
- No index! (simpler, more SQL-like)
- Uses null instead of NaN for missing values
- Different API (but more consistent)

TASK:
1. Create a Polars DataFrame from a dict
2. Create from list of dicts
3. Get shape and column names
"""
import polars as pl

# ---- YOUR CODE HERE ----
# Task 1: Create DataFrame from dict
# Columns: name, age, city
# Data: Alice/30/NYC, Bob/25/LA, Carol/35/Chicago
df_from_dict = None

# Task 2: Create from list of dicts (same data)
df_from_records = None

# Task 3: Get properties
num_rows = None       # Number of rows
num_cols = None       # Number of columns
column_names = None   # List of column names
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    expected = pl.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "age": [30, 25, 35],
        "city": ["NYC", "LA", "Chicago"]
    })

    print("Task 1: DataFrame from dict")
    check(df_from_dict.equals(expected), expected=True,
          hint='pl.DataFrame({"name": [...], "age": [...], "city": [...]})')

    print("\nTask 2: DataFrame from records")
    check(df_from_records.equals(expected), expected=True)

    print("\nTask 3a: Number of rows")
    check(num_rows, expected=3,
          hint="df.height or df.shape[0]")

    print("\nTask 3b: Number of columns")
    check(num_cols, expected=3,
          hint="df.width or df.shape[1]")

    print("\nTask 3c: Column names")
    check(column_names, expected=["name", "age", "city"],
          hint="df.columns")
