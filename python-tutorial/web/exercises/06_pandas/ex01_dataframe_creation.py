"""
EXERCISE 1: DataFrame Creation

R vs Python:
    R:      data.frame(name=c("A","B"), val=c(1,2))
    Python: pd.DataFrame({"name": ["A","B"], "val": [1,2]})

Multiple ways to create DataFrames:

1. From dict of lists (column-oriented):
    pd.DataFrame({"col1": [1,2,3], "col2": [4,5,6]})

2. From list of dicts (row-oriented):
    pd.DataFrame([{"col1": 1, "col2": 4}, {"col1": 2, "col2": 5}])

3. From NumPy array:
    pd.DataFrame(arr, columns=["a", "b", "c"])

Key difference from R:
- pandas has an INDEX (row labels), R has row.names
- pandas columns are Series objects
- dtype is inferred but can be specified

TASK:
1. Create a DataFrame from a dict of lists
2. Create a DataFrame from a list of dicts
3. Check the shape, columns, and dtypes
"""
import pandas as pd
import numpy as np

# ---- YOUR CODE HERE ----
# Task 1: Create DataFrame from dict of lists
# Columns: name, age, salary
# Data: Alice/30/50000, Bob/25/60000, Carol/35/55000
df_from_dict = None

# Task 2: Create DataFrame from list of dicts (same data)
df_from_records = None

# Task 3: Get these properties from df_from_dict
num_rows = None      # Number of rows
num_cols = None      # Number of columns
column_names = None  # List of column names
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    expected_df = pd.DataFrame({
        "name": ["Alice", "Bob", "Carol"],
        "age": [30, 25, 35],
        "salary": [50000, 60000, 55000]
    })

    print("Task 1: DataFrame from dict")
    check(df_from_dict.equals(expected_df), expected=True,
          hint='pd.DataFrame({"name": [...], "age": [...], "salary": [...]})')

    print("\nTask 2: DataFrame from records")
    check(df_from_records.equals(expected_df), expected=True,
          hint='pd.DataFrame([{"name": "Alice", ...}, {...}, {...}])')

    print("\nTask 3a: Number of rows")
    check(num_rows, expected=3,
          hint="df.shape[0] or len(df)")

    print("\nTask 3b: Number of columns")
    check(num_cols, expected=3,
          hint="df.shape[1] or len(df.columns)")

    print("\nTask 3c: Column names")
    check(list(column_names), expected=["name", "age", "salary"],
          hint="list(df.columns)")
