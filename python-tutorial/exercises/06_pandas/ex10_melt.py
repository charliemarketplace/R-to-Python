"""
EXERCISE 10: Reshaping - Wide to Long (melt)

R vs Python:
    R:      pivot_longer(df, cols=c("a","b"), names_to="var", values_to="val")
    Python: df.melt(id_vars=["id"], value_vars=["a","b"],
                    var_name="var", value_name="val")

melt() converts wide format to long format (unpivot).

Wide format:
    id  Q1   Q2   Q3
    A   10   20   30
    B   15   25   35

Long format:
    id  quarter  sales
    A   Q1       10
    A   Q2       20
    A   Q3       30
    B   Q1       15
    ...

melt() arguments:
    id_vars     - Columns to keep as identifiers
    value_vars  - Columns to unpivot (default: all not in id_vars)
    var_name    - Name for the "variable" column
    value_name  - Name for the "value" column

TASK:
Given wide sales data by quarter:
1. Melt to long format with 'product' as id, quarters as variables
2. Name the columns appropriately: "quarter" and "sales"
"""
import pandas as pd

wide_sales = pd.DataFrame({
    "product": ["Widget", "Gadget", "Gizmo"],
    "Q1": [100, 150, 80],
    "Q2": [120, 140, 90],
    "Q3": [130, 160, 100],
    "Q4": [140, 155, 110]
})

# ---- YOUR CODE HERE ----
# Melt to long format:
# - Keep 'product' as identifier
# - Melt Q1, Q2, Q3, Q4 columns
# - Name variable column "quarter"
# - Name value column "sales"
long_sales = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Checking long format structure:")
    check(set(long_sales.columns), expected={"product", "quarter", "sales"},
          hint='melt(id_vars=["product"], var_name="quarter", value_name="sales")')

    print("\nChecking number of rows:")
    check(len(long_sales), expected=12,
          hint="3 products x 4 quarters = 12 rows")

    print("\nChecking quarters column:")
    check(set(long_sales["quarter"]), expected={"Q1", "Q2", "Q3", "Q4"})

    print("\nChecking a specific value:")
    widget_q1 = long_sales[(long_sales["product"] == "Widget") &
                           (long_sales["quarter"] == "Q1")]["sales"].iloc[0]
    check(widget_q1, expected=100)
