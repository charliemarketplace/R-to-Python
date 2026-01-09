"""
EXERCISE 6: GroupBy Operations - SOLUTION
"""
import pandas as pd

sales = pd.DataFrame({
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "region": ["East", "East", "West", "West", "East"],
    "units": [100, 150, 80, 120, 90],
    "price": [500.0, 50.0, 600.0, 40.0, 550.0]
})

# ---- YOUR CODE HERE ----
# Task 1: Mean price per category (result should be a Series)
mean_price = sales.groupby("category")["price"].mean()

# Task 2: Total units per category
total_units = sales.groupby("category")["units"].sum()

# Task 3: Multiple aggs - sum of units, mean of price
multi_agg = sales.groupby("category").agg({"units": "sum", "price": "mean"})

# Task 4: Group by category AND region, sum of units
by_cat_region = sales.groupby(["category", "region"])["units"].sum()
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Mean price per category")
    check(mean_price["Electronics"], expected=550.0, rtol=0.01,
          hint='sales.groupby("category")["price"].mean()')
    check(mean_price["Clothing"], expected=45.0, rtol=0.01)

    print("\nTask 2: Total units per category")
    check(total_units["Electronics"], expected=270)
    check(total_units["Clothing"], expected=270)

    print("\nTask 3: Multiple aggregations")
    check(multi_agg.loc["Electronics", "units"], expected=270,
          hint='groupby("category").agg({"units": "sum", "price": "mean"})')

    print("\nTask 4: Group by category and region")
    if hasattr(by_cat_region, 'reset_index'):
        result = by_cat_region
        if isinstance(result.index, pd.MultiIndex):
            result = result.reset_index()
    check("units" in str(by_cat_region) or by_cat_region is not None, expected=True,
          hint='sales.groupby(["category", "region"])["units"].sum()')
