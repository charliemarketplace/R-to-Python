"""
EXERCISE 6: List of Dicts - Record-Oriented Data

This is THE most common data structure for JSON/API data!

R equivalent: A list of named lists, or rows of a data.frame

Structure:
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
    ]

Access patterns:
    users[0]           # First record: {"name": "Alice", "age": 30}
    users[0]["name"]   # "Alice"
    users[1]["age"]    # 25

Extract a "column" (like a data.frame column):
    names = [u["name"] for u in users]  # ["Alice", "Bob"]

Filter records:
    adults = [u for u in users if u["age"] >= 18]

This structure converts easily to pandas:
    import pandas as pd
    df = pd.DataFrame(users)

TASK:
Given the employees list:
1. Get the name of the third employee
2. Create a list of all salaries
3. Filter to employees in the "Engineering" department
4. Calculate the average salary
"""

employees = [
    {"name": "Alice", "dept": "Engineering", "salary": 95000},
    {"name": "Bob", "dept": "Marketing", "salary": 75000},
    {"name": "Carol", "dept": "Engineering", "salary": 105000},
    {"name": "Dave", "dept": "Sales", "salary": 80000},
    {"name": "Eve", "dept": "Engineering", "salary": 90000},
]

# ---- YOUR CODE HERE ----
# Task 1: Name of third employee
third_name = None

# Task 2: List of all salaries
salaries = None

# Task 3: List of dicts for Engineering employees only
engineers = None

# Task 4: Average salary (of all employees)
avg_salary = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Third employee name")
    check(third_name, expected="Carol",
          hint="employees[2]['name'] - remember 0-indexing!")

    print("\nTask 2: All salaries")
    check(salaries, expected=[95000, 75000, 105000, 80000, 90000],
          hint="[e['salary'] for e in employees]")

    print("\nTask 3: Engineering employees")
    expected_eng = [
        {"name": "Alice", "dept": "Engineering", "salary": 95000},
        {"name": "Carol", "dept": "Engineering", "salary": 105000},
        {"name": "Eve", "dept": "Engineering", "salary": 90000},
    ]
    check(engineers, expected=expected_eng,
          hint="[e for e in employees if e['dept'] == 'Engineering']")

    print("\nTask 4: Average salary")
    check(avg_salary, expected=89000.0, rtol=0.01,
          hint="sum(salaries) / len(salaries)")
