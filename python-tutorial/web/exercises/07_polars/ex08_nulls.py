"""
EXERCISE 8: Null Handling in Polars

pandas vs Polars:
    pandas: Uses NaN (float) for missing in numeric columns
    Polars: Uses null (proper null, any dtype)

Polars null handling is cleaner:
- null is distinct from NaN
- null works with any data type
- More SQL-like behavior

Key functions:
    pl.col("x").is_null()       # Boolean mask
    pl.col("x").is_not_null()
    pl.col("x").fill_null(value)
    pl.col("x").drop_nulls()

    df.drop_nulls()              # Drop rows with any null
    df.drop_nulls(subset=["col"])  # Check specific columns
    df.fill_null(value)          # Fill all nulls
    df.null_count()              # Count nulls per column

TASK:
Given the DataFrame with null values:
1. Count nulls per column
2. Drop rows where 'score' is null
3. Fill null scores with the mean score
4. Fill null names with "Unknown"
"""
import polars as pl

df = pl.DataFrame({
    "name": ["Alice", "Bob", None, "Dave", "Eve"],
    "score": [85.0, None, 90.0, None, 78.0],
    "grade": ["A", "B", "A", None, "C"]
})

# ---- YOUR CODE HERE ----
# Task 1: Count nulls per column
# Returns a DataFrame with null counts
null_counts = None

# Task 2: Drop rows where score is null
df_score_not_null = None

# Task 3: Fill null scores with mean
mean_score = df.select(pl.col("score").mean()).item()
df_filled_score = None

# Task 4: Fill null names with "Unknown"
df_filled_name = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Null counts")
    name_nulls = null_counts.select("name").item()
    check(name_nulls, expected=1,
          hint="df.null_count()")

    print("\nTask 2: Drop rows with null score")
    check(df_score_not_null.height, expected=3,
          hint='df.drop_nulls(subset=["score"])')

    print("\nTask 3: Fill null scores")
    check(df_filled_score["score"].null_count(), expected=0,
          hint='df.with_columns(pl.col("score").fill_null(mean_score))')

    print("\nTask 4: Fill null names")
    filled_names = df_filled_name["name"].to_list()
    check(filled_names[2], expected="Unknown",
          hint='df.with_columns(pl.col("name").fill_null("Unknown"))')
