"""
EXERCISE 11: Reshaping - Long to Wide (pivot)

R vs Python:
    R:      pivot_wider(df, names_from="var", values_from="val")
    Python: df.pivot(columns="var", values="val")
            df.pivot_table(columns="var", values="val", aggfunc="mean")

pivot() vs pivot_table():
    pivot()       - Reshape only, errors on duplicates
    pivot_table() - Reshape with aggregation (handles duplicates)

Long format:
    product  quarter  sales
    Widget   Q1       100
    Widget   Q2       120
    Gadget   Q1       150
    ...

Wide format:
    product   Q1    Q2    Q3    Q4
    Widget    100   120   130   140
    Gadget    150   140   160   155

pivot() arguments:
    index   - Column(s) to use as row index
    columns - Column to spread into multiple columns
    values  - Column containing the values

pivot_table() adds:
    aggfunc - How to aggregate duplicates (mean, sum, etc.)

TASK:
Given long sales data:
1. Pivot to wide format with products as rows, quarters as columns
2. Create a pivot table showing mean sales by product and quarter
"""
import pandas as pd

long_sales = pd.DataFrame({
    "product": ["Widget", "Widget", "Widget", "Widget",
                "Gadget", "Gadget", "Gadget", "Gadget"],
    "quarter": ["Q1", "Q2", "Q3", "Q4", "Q1", "Q2", "Q3", "Q4"],
    "sales": [100, 120, 130, 140, 150, 140, 160, 155]
})

# For pivot_table with duplicates
sales_with_dupes = pd.DataFrame({
    "product": ["Widget", "Widget", "Widget", "Gadget", "Gadget", "Gadget"],
    "quarter": ["Q1", "Q1", "Q2", "Q1", "Q1", "Q2"],  # Note: duplicate Q1s
    "sales": [100, 110, 120, 150, 160, 140]
})

# ---- YOUR CODE HERE ----
# Task 1: Pivot long_sales to wide format
# Rows = product, Columns = quarter, Values = sales
wide_sales = None

# Task 2: Pivot table with aggregation (mean)
# This handles the duplicate Q1 values in sales_with_dupes
pivot_mean = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Pivot to wide format")
    check("Q1" in wide_sales.columns, expected=True,
          hint='df.pivot(index="product", columns="quarter", values="sales")')
    check(wide_sales.loc["Widget", "Q1"], expected=100)
    check(wide_sales.loc["Gadget", "Q3"], expected=160)

    print("\nTask 2: Pivot table with mean aggregation")
    # Widget Q1 mean: (100 + 110) / 2 = 105
    check(pivot_mean.loc["Widget", "Q1"], expected=105.0,
          hint='df.pivot_table(index="product", columns="quarter", values="sales", aggfunc="mean")')
    # Gadget Q1 mean: (150 + 160) / 2 = 155
    check(pivot_mean.loc["Gadget", "Q1"], expected=155.0)
