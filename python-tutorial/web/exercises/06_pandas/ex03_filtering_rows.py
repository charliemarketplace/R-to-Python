"""
EXERCISE 3: Filtering Rows (Boolean Indexing)

R vs Python:
    R:      filter(df, age > 30)
            df[df$age > 30, ]
    Python: df[df["age"] > 30]
            df.query("age > 30")

Boolean indexing works like NumPy:
    mask = df["age"] > 30    # Boolean Series
    df[mask]                  # Rows where mask is True

Compound conditions (use &, |, ~ with parentheses):
    R:      filter(df, age > 25 & salary > 80000)
    Python: df[(df["age"] > 25) & (df["salary"] > 80000)]

    & = and, | = or, ~ = not

Alternative: query() method (cleaner for complex conditions)
    df.query("age > 25 and salary > 80000")
    df.query("dept == 'Eng'")  # Note: string needs quotes

TASK:
Given the employees DataFrame:
1. Filter to employees with salary > 85000
2. Filter to Engineering department
3. Filter: Eng dept AND salary > 80000
4. Filter: salary > 90000 OR years >= 5
"""
import pandas as pd

employees = pd.DataFrame({
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
    check(list(high_earners["name"]), expected=["Alice", "Carol"],
          hint='df[df["salary"] > 85000]')

    print("\nTask 2: Engineering dept")
    check(list(engineers["name"]), expected=["Alice", "Carol", "Eve"],
          hint='df[df["dept"] == "Eng"]')

    print("\nTask 3: Eng AND salary > 80000")
    check(list(senior_engineers["name"]), expected=["Alice", "Carol", "Eve"],
          hint='df[(df["dept"] == "Eng") & (df["salary"] > 80000)]')

    print("\nTask 4: salary > 90000 OR years >= 5")
    check(set(experienced_or_high["name"]), expected={"Alice", "Carol"},
          hint='df[(df["salary"] > 90000) | (df["years"] >= 5)]')
