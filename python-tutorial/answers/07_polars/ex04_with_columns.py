"""
EXERCISE 4: Adding/Modifying Columns with with_columns() - SOLUTION
"""
import polars as pl

sales = pl.DataFrame({
    "product": ["A", "B", "C", "D"],
    "units": [100, 150, 80, 200],
    "price": [10.0, 15.0, 25.0, 8.0],
    "cost": [6.0, 9.0, 15.0, 5.0]
})

# ---- YOUR CODE HERE ----
# Task 1: Add 'total' column
sales_with_total = sales.with_columns(
    (pl.col("units") * pl.col("price")).alias("total")
)

# Task 2: Add 'discount_price' to sales_with_total
sales_with_discount = sales_with_total.with_columns(
    (pl.col("price") * 0.9).alias("discount_price")
)

# Task 3: Add 'profit_margin'
sales_with_margin = sales_with_discount.with_columns(
    ((pl.col("price") - pl.col("cost")) / pl.col("price")).alias("profit_margin")
)

# Task 4: Do all three in one with_columns() call
sales_all = sales.with_columns(
    (pl.col("units") * pl.col("price")).alias("total"),
    (pl.col("price") * 0.9).alias("discount_price"),
    ((pl.col("price") - pl.col("cost")) / pl.col("price")).alias("profit_margin")
)
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Total column")
    check(sales_with_total["total"].to_list(), expected=[1000.0, 2250.0, 2000.0, 1600.0],
          hint='df.with_columns((pl.col("units") * pl.col("price")).alias("total"))')

    print("\nTask 2: Discount price")
    check(sales_with_discount["discount_price"].to_list(), expected=[9.0, 13.5, 22.5, 7.2],
          hint='(pl.col("price") * 0.9).alias("discount_price")')

    print("\nTask 3: Profit margin")
    expected_margin = [0.4, 0.4, 0.4, 0.375]
    actual = sales_with_margin["profit_margin"].to_list()
    check([round(x, 3) for x in actual], expected=expected_margin)

    print("\nTask 4: All columns at once")
    check("total" in sales_all.columns, expected=True)
    check("discount_price" in sales_all.columns, expected=True)
    check("profit_margin" in sales_all.columns, expected=True)
