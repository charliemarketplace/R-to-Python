"""
EXERCISE 7: Aggregations with axis Parameter

R vs Python:
    R:      colMeans(mat)     # Mean of each column
            rowMeans(mat)     # Mean of each row
            sum(mat)          # Total sum
    Python: mat.mean(axis=0)  # Mean of each column
            mat.mean(axis=1)  # Mean of each row
            mat.sum()         # Total sum

The axis parameter:
    axis=None  -> Aggregate over ALL elements (default)
    axis=0     -> Aggregate along rows (result per column)
    axis=1     -> Aggregate along columns (result per row)

Think of it as: "collapse this axis"
    axis=0 collapses rows -> one value per column
    axis=1 collapses columns -> one value per row

Common aggregations:
    .sum(), .mean(), .std(), .var()
    .min(), .max(), .argmin(), .argmax()
    .cumsum(), .cumprod()

TASK:
Given the 3x4 matrix of sales data (rows=stores, cols=quarters):
1. Total sales (sum of everything)
2. Sales per store (sum each row)
3. Sales per quarter (sum each column)
4. Best quarter per store (argmax of each row)
"""
import numpy as np

# Sales data: 3 stores, 4 quarters
sales = np.array([
    [100, 120, 110, 130],  # Store 1
    [90, 100, 120, 140],   # Store 2
    [150, 140, 130, 120],  # Store 3
])

# ---- YOUR CODE HERE ----
total_sales = None        # Single number
sales_per_store = None    # Shape (3,) - one per store
sales_per_quarter = None  # Shape (4,) - one per quarter
best_quarter = None       # Shape (3,) - quarter index with max sales per store
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Total sales")
    check(total_sales, expected=1450,
          hint="sales.sum() or sales.sum(axis=None)")

    print("\nTask 2: Sales per store")
    check(sales_per_store, expected=np.array([460, 450, 540]),
          hint="sales.sum(axis=1) - sum across columns for each row")

    print("\nTask 3: Sales per quarter")
    check(sales_per_quarter, expected=np.array([340, 360, 360, 390]),
          hint="sales.sum(axis=0) - sum across rows for each column")

    print("\nTask 4: Best quarter per store")
    check(best_quarter, expected=np.array([3, 3, 0]),
          hint="sales.argmax(axis=1) - index of max in each row")
