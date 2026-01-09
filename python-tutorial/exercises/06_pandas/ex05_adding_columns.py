"""
EXERCISE 5: Adding/Modifying Columns (mutate equivalent)

R vs Python:
    R:      mutate(df, new_col = a + b)
    Python: df["new_col"] = df["a"] + df["b"]  # In-place
            df.assign(new_col = df["a"] + df["b"])  # Returns copy

Ways to add columns:
    # Direct assignment (modifies df in place)
    df["new"] = df["a"] + df["b"]

    # assign() method (returns new DataFrame, doesn't modify original)
    df.assign(new = df["a"] + df["b"])

    # assign() with lambda (useful in chains)
    df.assign(new = lambda x: x["a"] + x["b"])

The assign() method is more "functional" (like tidyverse):
    df.assign(
        total = df["a"] + df["b"],
        avg = lambda x: x["total"] / 2  # Can reference just-created columns
    )

TASK:
Given the sales DataFrame:
1. Add a 'total' column (units * price)
2. Add a 'discount_price' column (price * 0.9)
3. Add a 'profit_margin' column: (price - cost) / price
4. Use assign() to add 'taxed_total' (total * 1.08) without modifying original
"""
import pandas as pd

sales = pd.DataFrame({
    "product": ["A", "B", "C", "D"],
    "units": [100, 150, 80, 200],
    "price": [10.0, 15.0, 25.0, 8.0],
    "cost": [6.0, 9.0, 15.0, 5.0]
})

# ---- YOUR CODE HERE ----
# Task 1: Add 'total' column (in-place is fine)
sales["total"] = None

# Task 2: Add 'discount_price' column (in-place is fine)
sales["discount_price"] = None

# Task 3: Add 'profit_margin' column
sales["profit_margin"] = None

# Task 4: Create new DataFrame with 'taxed_total' using assign()
# Do NOT modify the original sales DataFrame for this one
sales_with_tax = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Total column")
    check(list(sales["total"]), expected=[1000.0, 2250.0, 2000.0, 1600.0],
          hint='sales["total"] = sales["units"] * sales["price"]')

    print("\nTask 2: Discount price")
    check(list(sales["discount_price"]), expected=[9.0, 13.5, 22.5, 7.2],
          hint='sales["discount_price"] = sales["price"] * 0.9')

    print("\nTask 3: Profit margin")
    expected_margin = [0.4, 0.4, 0.4, 0.375]
    check(list(sales["profit_margin"]), expected=expected_margin,
          hint='(price - cost) / price')

    print("\nTask 4: Taxed total (using assign)")
    expected_taxed = [1080.0, 2430.0, 2160.0, 1728.0]
    check(list(sales_with_tax["taxed_total"]), expected=expected_taxed,
          hint='sales.assign(taxed_total = sales["total"] * 1.08)')
