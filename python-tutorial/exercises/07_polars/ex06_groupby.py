"""
EXERCISE 6: GroupBy and Aggregation

pandas vs Polars:
    pandas: df.groupby("cat")["val"].mean()
    Polars: df.group_by("cat").agg(pl.col("val").mean())

Polars groupby syntax:

    df.group_by("category").agg(
        pl.col("value").mean().alias("avg_value"),
        pl.col("value").sum().alias("total_value"),
        pl.count().alias("count")
    )

Key differences from pandas:
- Use group_by() (with underscore)
- Must use agg() with expressions
- More explicit about what you're computing
- Can compute multiple aggregations in one call

Aggregation expressions:
    pl.col("x").mean()
    pl.col("x").sum()
    pl.col("x").count()
    pl.count()  # Count rows
    pl.col("x").first() / .last()
    pl.col("x").n_unique()

TASK:
Given the sales DataFrame:
1. Mean price per category
2. Total units per category
3. Multiple aggregations: count, sum units, mean price per category
4. Group by category AND region
"""
import polars as pl

sales = pl.DataFrame({
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "region": ["East", "East", "West", "West", "East"],
    "units": [100, 150, 80, 120, 90],
    "price": [500.0, 50.0, 600.0, 40.0, 550.0]
})

# ---- YOUR CODE HERE ----
# Task 1: Mean price per category
mean_price = None

# Task 2: Total units per category
total_units = None

# Task 3: Multiple aggregations per category
# - count (number of rows)
# - total_units (sum of units)
# - avg_price (mean of price)
multi_agg = None

# Task 4: Group by category AND region, sum of units
by_cat_region = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Mean price per category")
    elec_price = mean_price.filter(pl.col("category") == "Electronics")["price"][0]
    check(elec_price, expected=550.0, rtol=0.01,
          hint='df.group_by("category").agg(pl.col("price").mean())')

    print("\nTask 2: Total units per category")
    elec_units = total_units.filter(pl.col("category") == "Electronics")["units"][0]
    check(elec_units, expected=270)

    print("\nTask 3: Multiple aggregations")
    check("count" in multi_agg.columns or "n" in str(multi_agg.columns).lower(), expected=True,
          hint='Include pl.count().alias("count")')

    print("\nTask 4: Group by category and region")
    check(by_cat_region.shape[0] >= 3, expected=True,
          hint='df.group_by(["category", "region"]).agg(...)')
