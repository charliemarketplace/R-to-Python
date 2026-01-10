"""
EXERCISE 2: Selecting Columns with select()

pandas vs Polars:
    pandas: df["col"], df[["a", "b"]]
    Polars: df.select("col"), df.select(["a", "b"])

Polars uses select() for column selection:

    df.select("name")                    # Single column
    df.select(["name", "age"])          # Multiple columns
    df.select(pl.col("name"))           # Using expression
    df.select(pl.col("name", "age"))    # Multiple with expression

Why expressions? They're composable and powerful:
    df.select(
        pl.col("name"),
        pl.col("age") * 2,  # Transform while selecting
        pl.col("salary").mean()  # Aggregate
    )

Note: select() ALWAYS returns a DataFrame (not Series like pandas).

TASK:
Given the employees DataFrame:
1. Select the 'name' column
2. Select 'name' and 'salary' columns
3. Select all columns except 'dept'
"""
import polars as pl

employees = pl.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave"],
    "dept": ["Eng", "Sales", "Eng", "HR"],
    "salary": [90000, 80000, 95000, 70000],
    "years": [5, 3, 7, 2]
})

# ---- YOUR CODE HERE ----
# Task 1: Select 'name' column (returns DataFrame with 1 column)
name_df = None

# Task 2: Select 'name' and 'salary'
name_salary = None

# Task 3: Select all except 'dept'
# Hint: df.select(pl.exclude("dept")) or df.drop("dept")
without_dept = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: name column")
    check(name_df.columns, expected=["name"],
          hint='df.select("name")')
    check(name_df["name"].to_list(), expected=["Alice", "Bob", "Carol", "Dave"])

    print("\nTask 2: name and salary")
    check(set(name_salary.columns), expected={"name", "salary"},
          hint='df.select(["name", "salary"])')

    print("\nTask 3: All except dept")
    check(set(without_dept.columns), expected={"name", "salary", "years"},
          hint='df.select(pl.exclude("dept")) or df.drop("dept")')
