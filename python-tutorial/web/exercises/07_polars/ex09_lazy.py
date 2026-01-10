"""
EXERCISE 9: Lazy Evaluation

Polars has two modes:
- Eager: Operations execute immediately (like pandas)
- Lazy: Operations are recorded, then optimized and executed together

Lazy evaluation benefits:
- Query optimization (predicate pushdown, projection pushdown)
- Reduced memory usage
- Faster execution for complex queries

Creating lazy frames:
    lf = df.lazy()               # From DataFrame
    lf = pl.scan_csv("file.csv") # Lazy read (nothing loaded yet!)

Working with lazy frames:
    lf = (
        df.lazy()
        .filter(pl.col("x") > 0)
        .group_by("cat")
        .agg(pl.col("y").mean())
    )
    result = lf.collect()  # Execute and get DataFrame

Key methods:
    .lazy()    # Convert DataFrame to LazyFrame
    .collect() # Execute LazyFrame, return DataFrame
    .explain() # Show query plan (for debugging)

TASK:
1. Convert DataFrame to lazy
2. Build a lazy query with filter and aggregation
3. Execute with collect()
4. Use explain() to see the query plan
"""
import polars as pl

sales = pl.DataFrame({
    "product": ["Widget", "Gadget", "Widget", "Gizmo", "Gadget", "Widget"],
    "region": ["East", "East", "West", "West", "West", "East"],
    "amount": [100, 150, 120, 80, 200, 90]
})

# ---- YOUR CODE HERE ----
# Task 1: Convert to lazy frame
lazy_sales = None

# Task 2: Build a lazy query:
# - Filter to region == "East"
# - Group by product
# - Calculate sum of amount
# (Don't collect yet!)
lazy_query = None

# Task 3: Execute the query
result = None

# Task 4: Get the query plan as a string
# Hint: Use explain() method
query_plan = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Lazy frame created")
    check(str(type(lazy_sales).__name__), expected="LazyFrame",
          hint="df.lazy()")

    print("\nTask 2: Lazy query built")
    check(str(type(lazy_query).__name__), expected="LazyFrame",
          hint="lazy_sales.filter(...).group_by(...).agg(...)")

    print("\nTask 3: Result collected")
    widget_sum = result.filter(pl.col("product") == "Widget")["amount"][0]
    check(widget_sum, expected=190,  # East widgets: 100 + 90
          hint="lazy_query.collect()")

    print("\nTask 4: Query plan")
    check(query_plan is not None and len(query_plan) > 0, expected=True,
          hint="lazy_query.explain()")
    print("Query plan preview:", query_plan[:200] if query_plan else "None")
