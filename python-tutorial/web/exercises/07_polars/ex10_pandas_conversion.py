"""
EXERCISE 10: Converting Between Pandas and Polars

You'll often need to convert between pandas and Polars:
- Use pandas for libraries that require it (e.g., sklearn)
- Use Polars for fast data processing
- Convert at boundaries

Pandas to Polars:
    pl_df = pl.from_pandas(pd_df)

Polars to Pandas:
    pd_df = pl_df.to_pandas()

Converting Series:
    pl_series = pl.from_pandas(pd_series)
    pd_series = pl_series.to_pandas()

Note on indexes:
- Polars doesn't have indexes
- When converting from pandas, index becomes a column or is lost
- When converting to pandas, no special index (just 0, 1, 2, ...)

TASK:
1. Convert a pandas DataFrame to Polars
2. Process in Polars (faster operations)
3. Convert back to pandas
4. Handle a pandas DataFrame with non-default index
"""
import pandas as pd
import polars as pl
import numpy as np

# Pandas DataFrame
pd_df = pd.DataFrame({
    "name": ["Alice", "Bob", "Carol"],
    "value": [10, 20, 30]
})

# Pandas DataFrame with custom index
pd_indexed = pd.DataFrame({
    "score": [85, 90, 78]
}, index=["Alice", "Bob", "Carol"])
pd_indexed.index.name = "student"

# ---- YOUR CODE HERE ----
# Task 1: Convert pd_df to Polars
pl_df = None

# Task 2: Double the 'value' column in Polars
pl_doubled = None

# Task 3: Convert back to pandas
pd_result = None

# Task 4: Convert pd_indexed to Polars (preserving index as column)
# Hint: reset_index() first, or use include_index parameter
pl_from_indexed = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check, check_type

    print("Task 1: Pandas to Polars")
    check_type(pl_df, pl.DataFrame,
               hint="pl.from_pandas(pd_df)")

    print("\nTask 2: Process in Polars")
    check(pl_doubled["value"].to_list(), expected=[20, 40, 60],
          hint='df.with_columns((pl.col("value") * 2).alias("value"))')

    print("\nTask 3: Back to pandas")
    check_type(pd_result, pd.DataFrame,
               hint="pl_df.to_pandas()")

    print("\nTask 4: Indexed DataFrame conversion")
    check("student" in pl_from_indexed.columns, expected=True,
          hint="pd_indexed.reset_index() first, then pl.from_pandas()")
    check(pl_from_indexed["student"].to_list(), expected=["Alice", "Bob", "Carol"])
