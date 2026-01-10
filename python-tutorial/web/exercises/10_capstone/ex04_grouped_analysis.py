"""
CAPSTONE EXERCISE 4: Grouped Analysis

Perform aggregations and grouped calculations:
1. Summary statistics by department
2. Summary statistics by salary band
3. Cross-tabulations
4. Identify patterns
"""
import pandas as pd
import numpy as np
from datetime import datetime

# ---- TRANSFORMED DATASET ----
np.random.seed(42)
n = 100
TODAY = datetime(2024, 6, 1)

df = pd.DataFrame({
    "employee_id": range(1001, 1001 + n),
    "department": np.random.choice(["Engineering", "Sales", "Marketing", "HR"], n),
    "salary": np.random.normal(75000, 15000, n).round(2),
    "hire_date": pd.to_datetime(
        np.random.choice(pd.date_range("2015-01-01", "2024-01-01", freq="D"), n)
    ),
    "age": np.random.randint(22, 65, n),
    "rating": np.random.choice([1.0, 2.0, 3.0, 4.0, 5.0], n, p=[0.05, 0.1, 0.35, 0.35, 0.15]),
})

df["tenure_years"] = (TODAY - df["hire_date"]).dt.days / 365.25
df["salary_band"] = pd.cut(df["salary"], bins=[0, 60000, 90000, float('inf')],
                           labels=["Low", "Medium", "High"])
df["age_group"] = pd.cut(df["age"], bins=[0, 30, 40, 50, 100],
                         labels=["20s", "30s", "40s", "50+"])
df["high_performer"] = df["rating"] >= 4

# ---- YOUR CODE HERE ----
# Task 1: Department summary
# Calculate per department: count, mean salary, mean rating, mean tenure
# Result should be a DataFrame with department as index
dept_summary = None

# Task 2: Salary band summary
# Count and mean rating per salary band
band_summary = None

# Task 3: Cross-tabulation: department vs salary band (counts)
# Hint: pd.crosstab(df["department"], df["salary_band"])
dept_band_crosstab = None

# Task 4: High performer rate by department
# What percentage of each department are high performers?
# Result should be a Series with department as index
hp_rate_by_dept = None

# Task 5: Find the department with highest average salary
highest_salary_dept = None  # String: department name
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Grouped Analysis ===\n")

    print("Task 1: Department summary")
    check(dept_summary is not None, expected=True)
    check("salary" in str(dept_summary.columns).lower() or "mean" in str(dept_summary.columns).lower(),
          expected=True,
          hint='df.groupby("department").agg({...})')
    print(dept_summary)

    print("\nTask 2: Salary band summary")
    check(band_summary is not None, expected=True,
          hint='df.groupby("salary_band").agg({...})')
    print(band_summary)

    print("\nTask 3: Crosstab")
    check(dept_band_crosstab is not None, expected=True,
          hint='pd.crosstab(df["department"], df["salary_band"])')
    print(dept_band_crosstab)

    print("\nTask 4: High performer rate by department")
    check(hp_rate_by_dept is not None, expected=True,
          hint='df.groupby("department")["high_performer"].mean()')
    print(hp_rate_by_dept)

    print("\nTask 5: Highest salary department")
    expected_highest = df.groupby("department")["salary"].mean().idxmax()
    check(highest_salary_dept == expected_highest, expected=True,
          hint='df.groupby("department")["salary"].mean().idxmax()')
    print(f"Department with highest avg salary: {highest_salary_dept}")
