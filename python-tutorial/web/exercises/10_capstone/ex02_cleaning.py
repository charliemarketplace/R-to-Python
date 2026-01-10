"""
CAPSTONE EXERCISE 2: Data Cleaning

Now that you've identified issues, let's clean the data:
1. Remove duplicates
2. Standardize department names
3. Handle missing values
4. Fix invalid ages
5. Convert data types appropriately
"""
import pandas as pd
import numpy as np

# ---- DATASET (same as ex01) ----
np.random.seed(42)
n = 100
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
        -1
    ),
    "rating": np.random.choice([1, 2, 3, 4, 5, "N/A", None], n),
})
raw_data = pd.concat([raw_data, raw_data.iloc[:3]], ignore_index=True)

# ---- YOUR CODE HERE ----
# Start with a copy
df = raw_data.copy()

# Task 1: Remove duplicate rows
# Hint: df.drop_duplicates()


# Task 2: Standardize department names (title case: "Engineering", "Sales", etc.)
# Also fill null departments with "Unknown"
# Hint: df["department"].str.title(), fillna()


# Task 3: Handle missing salaries - fill with median salary
# Hint: df["salary"].fillna(df["salary"].median())


# Task 4: Fix invalid ages (replace -1 with NaN, then fill with median)
# Hint: df["age"].replace(-1, np.nan), then fillna


# Task 5: Convert hire_date to datetime
# Hint: pd.to_datetime(df["hire_date"])


# Task 6: Clean rating column - convert "N/A" to NaN, then to numeric
# Hint: df["rating"].replace("N/A", np.nan).astype(float)


# Final cleaned DataFrame should be in `df`
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Data Cleaning ===\n")

    print("Task 1: Remove duplicates")
    check(len(df) == 100, expected=True,
          hint="df = df.drop_duplicates()")

    print("\nTask 2: Standardize departments")
    dept_values = set(df["department"].dropna().unique())
    expected_depts = {"Engineering", "Sales", "Marketing", "Hr", "Unknown"}
    check(df["department"].isna().sum() == 0, expected=True,
          hint="No nulls - fill with 'Unknown'")
    print(f"Department values: {dept_values}")

    print("\nTask 3: Handle missing salaries")
    check(df["salary"].isna().sum() == 0, expected=True,
          hint="df['salary'] = df['salary'].fillna(df['salary'].median())")

    print("\nTask 4: Fix invalid ages")
    check((df["age"] < 0).sum() == 0, expected=True,
          hint="No negative ages after cleaning")

    print("\nTask 5: Convert hire_date")
    check(pd.api.types.is_datetime64_any_dtype(df["hire_date"]), expected=True,
          hint="df['hire_date'] = pd.to_datetime(df['hire_date'])")

    print("\nTask 6: Clean ratings")
    check("N/A" not in df["rating"].values, expected=True,
          hint="Replace 'N/A' with np.nan")

    print("\n--- Cleaned Data Summary ---")
    print(df.info())
    print("\n--- Sample ---")
    print(df.head())
