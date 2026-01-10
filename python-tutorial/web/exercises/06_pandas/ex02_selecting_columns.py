"""
EXERCISE 2: Selecting Columns

R vs Python:
    R:      df$col, df[,"col"], df[,c("a","b")]
    Python: df["col"], df[["a","b"]]

IMPORTANT difference:
    df["col"]     -> Returns a Series (1D, like a vector)
    df[["col"]]   -> Returns a DataFrame (2D, single column)
    df[["a","b"]] -> Returns a DataFrame (multiple columns)

This matters for chaining operations!

R's select() equivalent:
    # R: select(df, name, age)
    # Python:
    df[["name", "age"]]

Attribute access (convenient but limited):
    df.col_name  # Works for simple column names
    df.col_name  # FAILS if column name has spaces or conflicts with methods

TASK:
Given the employees DataFrame:
1. Select the 'name' column as a Series
2. Select the 'name' column as a DataFrame
3. Select multiple columns: name and salary
4. Select all columns except 'dept'
"""
import pandas as pd

employees = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave"],
    "dept": ["Eng", "Sales", "Eng", "HR"],
    "salary": [90000, 80000, 95000, 70000],
    "years": [5, 3, 7, 2]
})

# ---- YOUR CODE HERE ----
# Task 1: 'name' as Series
name_series = None

# Task 2: 'name' as DataFrame
name_df = None

# Task 3: Select name and salary
name_salary = None

# Task 4: All columns except 'dept'
without_dept = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check, check_type

    print("Task 1: name as Series")
    check_type(name_series, pd.Series,
               hint='df["col"] returns a Series')
    check(list(name_series), expected=["Alice", "Bob", "Carol", "Dave"])

    print("\nTask 2: name as DataFrame")
    check_type(name_df, pd.DataFrame,
               hint='df[["col"]] returns a DataFrame')
    check(list(name_df.columns), expected=["name"])

    print("\nTask 3: name and salary")
    check(list(name_salary.columns), expected=["name", "salary"],
          hint='df[["name", "salary"]]')

    print("\nTask 4: All except dept")
    check(set(without_dept.columns), expected={"name", "salary", "years"},
          hint='df[["name", "salary", "years"]] or df.drop(columns="dept")')
