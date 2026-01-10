"""
CAPSTONE EXERCISE 3: Data Transformation

Create derived features and transform the data:
1. Calculate tenure (years since hire)
2. Create salary bands
3. Create age groups
4. Calculate tenure-adjusted salary
"""
import pandas as pd
import numpy as np
from datetime import datetime

# ---- CLEANED DATASET ----
np.random.seed(42)
n = 100
df = pd.DataFrame({
    "employee_id": range(1001, 1001 + n),
    "name": [f"Employee_{i}" for i in range(n)],
    "department": np.random.choice(["Engineering", "Sales", "Marketing", "HR"], n),
    "salary": np.random.normal(75000, 15000, n).round(2),
    "hire_date": pd.to_datetime(
        np.random.choice(pd.date_range("2015-01-01", "2024-01-01", freq="D"), n)
    ),
    "age": np.random.randint(22, 65, n),
    "rating": np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0, np.nan], n),
})

# Reference date for tenure calculation
TODAY = datetime(2024, 6, 1)

# ---- YOUR CODE HERE ----
# Task 1: Calculate tenure in years
# tenure = (TODAY - hire_date).days / 365.25
df["tenure_years"] = None

# Task 2: Create salary bands
# "Low" if salary < 60000
# "Medium" if 60000 <= salary < 90000
# "High" if salary >= 90000
# Hint: Use pd.cut() or np.select()
df["salary_band"] = None

# Task 3: Create age groups
# "20s" if age < 30
# "30s" if 30 <= age < 40
# "40s" if 40 <= age < 50
# "50+" if age >= 50
df["age_group"] = None

# Task 4: Calculate salary per year of tenure
# (Avoid division by zero - use tenure_years.clip(lower=0.5))
df["salary_per_tenure"] = None

# Task 5: Create a "high_performer" flag (rating >= 4)
df["high_performer"] = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Data Transformation ===\n")

    print("Task 1: Tenure years")
    check("tenure_years" in df.columns, expected=True)
    check(df["tenure_years"].min() >= 0, expected=True,
          hint="(TODAY - df['hire_date']).dt.days / 365.25")

    print("\nTask 2: Salary bands")
    check("salary_band" in df.columns, expected=True)
    valid_bands = {"Low", "Medium", "High"}
    actual_bands = set(df["salary_band"].dropna().unique())
    check(actual_bands.issubset(valid_bands), expected=True,
          hint="Use pd.cut() with labels=['Low', 'Medium', 'High']")

    print("\nTask 3: Age groups")
    check("age_group" in df.columns, expected=True)
    valid_groups = {"20s", "30s", "40s", "50+"}
    actual_groups = set(df["age_group"].dropna().unique())
    check(actual_groups.issubset(valid_groups), expected=True)

    print("\nTask 4: Salary per tenure")
    check("salary_per_tenure" in df.columns, expected=True)
    check(df["salary_per_tenure"].isna().sum() == 0, expected=True,
          hint="Use clip(lower=0.5) to avoid division by zero")

    print("\nTask 5: High performer flag")
    check("high_performer" in df.columns, expected=True)
    check(df["high_performer"].dtype == bool, expected=True,
          hint="df['rating'] >= 4")

    print("\n--- Transformed Data ---")
    print(df[["name", "tenure_years", "salary_band", "age_group", "high_performer"]].head(10))
