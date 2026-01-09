"""
EXERCISE 5: Polars Expressions - The Heart of Polars

Expressions are composable building blocks in Polars.
They describe WHAT to compute, not HOW (Polars optimizes execution).

Basic expressions:
    pl.col("x")           # Reference a column
    pl.col("x", "y")      # Multiple columns
    pl.col("x") + 1       # Arithmetic
    pl.col("x").mean()    # Aggregation
    pl.col("x").alias("new_name")  # Rename result

Expression methods:
    .mean(), .sum(), .min(), .max(), .std()
    .abs(), .sqrt(), .log()
    .round(decimals)
    .cast(pl.Int64)       # Type conversion
    .is_null(), .is_not_null()
    .fill_null(value)

Chaining expressions:
    (pl.col("x") - pl.col("x").mean()) / pl.col("x").std()

String expressions:
    pl.col("name").str.to_uppercase()
    pl.col("name").str.contains("pattern")

TASK:
Given the scores DataFrame, use expressions to:
1. Calculate mean of scores
2. Calculate z-scores: (score - mean) / std
3. Create a "pass" column: True if score >= 70
4. Round scores to nearest 10
"""
import polars as pl

scores = pl.DataFrame({
    "student": ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "score": [85.0, 72.0, 91.0, 68.0, 79.0]
})

# ---- YOUR CODE HERE ----
# Task 1: Mean of scores (single value)
mean_score = None

# Task 2: Add z_score column
# z = (score - mean) / std
scores_with_z = None

# Task 3: Add 'pass' column (True if score >= 70)
scores_with_pass = None

# Task 4: Add 'rounded' column (round to nearest 10)
# Hint: (score / 10).round(0) * 10
scores_with_rounded = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Mean score")
    check(mean_score, expected=79.0, rtol=0.01,
          hint='scores.select(pl.col("score").mean()).item()')

    print("\nTask 2: Z-scores")
    check("z_score" in scores_with_z.columns, expected=True,
          hint='((pl.col("score") - pl.col("score").mean()) / pl.col("score").std())')
    # Check Alice's z-score: (85 - 79) / std
    alice_z = scores_with_z.filter(pl.col("student") == "Alice")["z_score"][0]
    check(abs(alice_z - 0.67) < 0.1, expected=True)

    print("\nTask 3: Pass column")
    check(scores_with_pass["pass"].to_list(), expected=[True, True, True, False, True],
          hint='(pl.col("score") >= 70).alias("pass")')

    print("\nTask 4: Rounded scores")
    check(scores_with_rounded["rounded"].to_list(), expected=[90.0, 70.0, 90.0, 70.0, 80.0],
          hint='((pl.col("score") / 10).round(0) * 10).alias("rounded")')
