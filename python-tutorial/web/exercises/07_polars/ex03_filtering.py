"""
EXERCISE 3: Filtering Rows with filter()

pandas vs Polars:
    pandas: df[df["age"] > 30]
    Polars: df.filter(pl.col("age") > 30)

Polars uses filter() with expressions:

    df.filter(pl.col("age") > 30)
    df.filter(pl.col("dept") == "Eng")

Compound conditions:
    df.filter(
        (pl.col("age") > 25) & (pl.col("salary") > 80000)
    )

    &  = and
    |  = or
    ~  = not

Note: The expression-based approach is more explicit and composable
than pandas' boolean indexing.

TASK:
Given the employees DataFrame:
1. Filter to employees with salary > 85000
2. Filter to Engineering department
3. Filter: Eng dept AND salary > 80000
4. Filter: salary > 90000 OR years >= 5
"""
import polars as pl

employees = pl.DataFrame({
    "name": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "dept": ["Eng", "Sales", "Eng", "HR", "Eng"],
    "salary": [90000, 80000, 95000, 70000, 85000],
    "years": [5, 3, 7, 2, 4]
})

# ---- YOUR CODE HERE ----
# Task 1: Salary > 85000
high_earners = None

# Task 2: Engineering department
engineers = None

# Task 3: Eng AND salary > 80000
senior_engineers = None

# Task 4: salary > 90000 OR years >= 5
experienced_or_high = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Salary > 85000")
    check(high_earners["name"].to_list(), expected=["Alice", "Carol"],
          hint='df.filter(pl.col("salary") > 85000)')

    print("\nTask 2: Engineering dept")
    check(engineers["name"].to_list(), expected=["Alice", "Carol", "Eve"],
          hint='df.filter(pl.col("dept") == "Eng")')

    print("\nTask 3: Eng AND salary > 80000")
    check(senior_engineers["name"].to_list(), expected=["Alice", "Carol", "Eve"],
          hint='df.filter((pl.col("dept") == "Eng") & (pl.col("salary") > 80000))')

    print("\nTask 4: salary > 90000 OR years >= 5")
    check(set(experienced_or_high["name"].to_list()), expected={"Alice", "Carol"},
          hint='df.filter((pl.col("salary") > 90000) | (pl.col("years") >= 5))')
