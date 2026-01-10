"""
EXERCISE 7: Dict of Lists - Column-Oriented Data

R equivalent: A data.frame IS a list of columns!
    data.frame(name = c("Alice", "Bob"), age = c(30, 25))

Python dict of lists:
    data = {
        "name": ["Alice", "Bob"],
        "age": [30, 25]
    }

This is perfect for creating DataFrames:
    import pandas as pd
    df = pd.DataFrame(data)  # Instant DataFrame!

Access patterns:
    data["name"]      # Whole column: ["Alice", "Bob"]
    data["name"][0]   # Single cell: "Alice"

Adding a column:
    data["city"] = ["NYC", "LA"]

Converting list-of-dicts to dict-of-lists:
    records = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]
    columns = {
        k: [r[k] for r in records]
        for k in records[0].keys()
    }

TASK:
1. Convert the employees list-of-dicts to dict-of-lists format
2. Add a new column "bonus" that is 10% of each salary
"""

employees = [
    {"name": "Alice", "salary": 95000},
    {"name": "Bob", "salary": 75000},
    {"name": "Carol", "salary": 105000},
]

# ---- YOUR CODE HERE ----
# Task 1: Convert to dict of lists
# Should be: {"name": ["Alice", "Bob", "Carol"], "salary": [95000, 75000, 105000]}
employee_columns = None

# Task 2: Add "bonus" column (10% of salary) to employee_columns
# After this, employee_columns should have a "bonus" key
# with values [9500.0, 7500.0, 10500.0]

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Dict of lists (name and salary)")
    # Check structure exists
    check(employee_columns.get("name"), expected=["Alice", "Bob", "Carol"])
    check(employee_columns.get("salary"), expected=[95000, 75000, 105000])

    print("\nTask 2: Bonus column added")
    check(employee_columns.get("bonus"), expected=[9500.0, 7500.0, 10500.0],
          hint="employee_columns['bonus'] = [s * 0.1 for s in employee_columns['salary']]")
