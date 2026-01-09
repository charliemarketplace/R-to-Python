"""
CAPSTONE EXERCISE 1: Load and Explore Data

SCENARIO:
You've been given a dataset of employee records from an HR system.
The data has various quality issues that you'll clean and analyze.

In this exercise, you'll:
1. Load the data
2. Examine its structure
3. Identify quality issues

This mimics a real data science workflow where you get messy data
and need to understand it before cleaning.
"""
import pandas as pd
import numpy as np

# ---- DATASET CREATION (Don't modify) ----
np.random.seed(42)
n = 100

# Create messy data
raw_data = pd.DataFrame({
    "employee_id": range(1001, 1001 + n),
    "name": [f"Employee_{i}" for i in range(n)],
    "department": np.random.choice(
        ["Engineering", "Sales", "Marketing", "HR", "engineering", "SALES", None],
        n
    ),
    "salary": np.where(
        np.random.random(n) > 0.1,
        np.random.normal(75000, 15000, n).round(2),
        np.nan
    ),
    "hire_date": pd.to_datetime(
        np.random.choice(pd.date_range("2015-01-01", "2024-01-01", freq="D"), n)
    ).astype(str),
    "age": np.where(
        np.random.random(n) > 0.05,
        np.random.randint(22, 65, n),
        -1  # Invalid ages
    ),
    "rating": np.random.choice([1, 2, 3, 4, 5, "N/A", None], n),
})
# Add some duplicates
raw_data = pd.concat([raw_data, raw_data.iloc[:3]], ignore_index=True)

# ---- YOUR CODE HERE ----
# Task 1: How many rows and columns?
n_rows = None
n_cols = None

# Task 2: What are the column names and dtypes?
# Store as a dictionary: {"column_name": "dtype_as_string", ...}
column_dtypes = None

# Task 3: How many missing values per column?
# Store as a dictionary: {"column_name": count, ...}
missing_counts = None

# Task 4: How many duplicate rows?
n_duplicates = None

# Task 5: What are the unique values in 'department' (including case variations)?
unique_departments = None  # Should be a set

# Task 6: Are there any invalid ages (negative or over 100)?
invalid_age_count = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Data Exploration ===\n")

    print("Task 1: Shape")
    check(n_rows, expected=103,  # 100 + 3 duplicates
          hint="len(raw_data) or raw_data.shape[0]")
    check(n_cols, expected=7,
          hint="raw_data.shape[1]")

    print("\nTask 2: Column dtypes")
    check(column_dtypes is not None and "employee_id" in column_dtypes, expected=True,
          hint="dict(raw_data.dtypes.astype(str))")

    print("\nTask 3: Missing values")
    check(missing_counts is not None, expected=True,
          hint="dict(raw_data.isna().sum())")

    print("\nTask 4: Duplicates")
    check(n_duplicates, expected=3,
          hint="raw_data.duplicated().sum()")

    print("\nTask 5: Unique departments")
    expected_depts = {"Engineering", "Sales", "Marketing", "HR",
                      "engineering", "SALES", None}
    check(unique_departments is not None, expected=True,
          hint="set(raw_data['department'].unique())")

    print("\nTask 6: Invalid ages")
    check(invalid_age_count >= 0, expected=True,
          hint="((raw_data['age'] < 0) | (raw_data['age'] > 100)).sum()")

    print("\n--- Data Preview ---")
    print(raw_data.head(10))
    print("\n--- Issues Found ---")
    print(f"Missing values: {dict(raw_data.isna().sum())}")
    print(f"Duplicate rows: {raw_data.duplicated().sum()}")
    print(f"Department variations: {raw_data['department'].unique()}")
