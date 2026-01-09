"""
EXERCISE 6: GroupBy Operations

R vs Python:
    R:      df %>% group_by(cat) %>% summarize(m = mean(val))
    Python: df.groupby("cat")["val"].mean()

GroupBy splits data into groups, applies a function, combines results.

Basic pattern:
    df.groupby("col").agg_func()
    df.groupby("col")["target"].agg_func()
    df.groupby(["col1", "col2"]).agg_func()

Common aggregations:
    .mean(), .sum(), .count(), .min(), .max()
    .std(), .var(), .first(), .last()
    .size()  # Count including NaN

Multiple aggregations:
    df.groupby("cat").agg({"col1": "mean", "col2": "sum"})

    # Named aggregations (pandas >= 0.25):
    df.groupby("cat").agg(
        mean_val = ("val", "mean"),
        total = ("val", "sum")
    )

TASK:
Given sales data:
1. Calculate mean price per category
2. Calculate total units sold per category
3. Multiple aggs: sum of units AND mean price per category
4. Group by category AND region, get sum of units
"""
import pandas as pd

sales = pd.DataFrame({
    "category": ["Electronics", "Clothing", "Electronics", "Clothing", "Electronics"],
    "region": ["East", "East", "West", "West", "East"],
    "units": [100, 150, 80, 120, 90],
    "price": [500, 50, 600, 40, 550]
})

# ---- YOUR CODE HERE ----
# Task 1: Mean price per category (result should be a Series)
mean_price = None

# Task 2: Total units per category
total_units = None

# Task 3: Multiple aggs - sum of units, mean of price
# Result should be a DataFrame with columns 'units' and 'price'
multi_agg = None

# Task 4: Group by category AND region, sum of units
by_cat_region = None
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
    # Reset index if it's a MultiIndex
    if hasattr(by_cat_region, 'reset_index'):
        result = by_cat_region
        if isinstance(result.index, pd.MultiIndex):
            result = result.reset_index()
    check("units" in str(by_cat_region) or by_cat_region is not None, expected=True,
          hint='sales.groupby(["category", "region"])["units"].sum()')
