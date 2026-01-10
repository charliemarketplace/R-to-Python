"""
EXERCISE 8: Handling Missing Values

R vs Python:
    R:      is.na(x), na.omit(df), replace_na(x, 0)
    Python: pd.isna(x), df.dropna(), df.fillna(0)

Missing value representations:
    Python: None, np.nan, pd.NA
    They all become NaN in numeric columns

Key functions:
    df.isna()       # Boolean mask of missing values
    df.notna()      # Boolean mask of non-missing
    df.dropna()     # Remove rows with ANY missing
    df.dropna(subset=["col"])  # Only check specific columns
    df.fillna(value)    # Replace NaN with value
    df.fillna({"col1": 0, "col2": "unknown"})  # Column-specific fills

Counting missing:
    df.isna().sum()           # Per column
    df.isna().sum().sum()     # Total

R's na.rm=TRUE equivalent:
    df["col"].sum()  # Ignores NaN by default!
    df["col"].mean(skipna=True)  # skipna=True is default

TASK:
Given the DataFrame with missing values:
1. Count missing values per column
2. Drop rows where 'score' is missing
3. Fill missing scores with the mean score
4. Fill missing names with "Unknown"
"""
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name": ["Alice", "Bob", None, "Dave", "Eve"],
    "score": [85, np.nan, 90, np.nan, 78],
    "grade": ["A", "B", "A", None, "C"]
})

# ---- YOUR CODE HERE ----
# Task 1: Count missing per column
missing_counts = None  # Should be a Series

# Task 2: Drop rows where score is missing
df_score_not_missing = None

# Task 3: Fill missing scores with mean (don't modify original df)
mean_score = df["score"].mean()  # Calculate mean of non-null scores
df_filled_score = None

# Task 4: Fill missing names with "Unknown" (don't modify original df)
df_filled_name = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Missing counts per column")
    check(missing_counts["name"], expected=1,
          hint="df.isna().sum()")
    check(missing_counts["score"], expected=2)
    check(missing_counts["grade"], expected=1)

    print("\nTask 2: Drop rows with missing score")
    check(len(df_score_not_missing), expected=3,
          hint='df.dropna(subset=["score"])')

    print("\nTask 3: Fill missing scores with mean")
    # Mean of [85, 90, 78] = 84.33...
    check(df_filled_score["score"].isna().sum(), expected=0,
          hint='df.fillna({"score": mean_score}) or df["score"].fillna(mean_score)')

    print("\nTask 4: Fill missing names")
    check(df_filled_name["name"].tolist()[2], expected="Unknown",
          hint='df.fillna({"name": "Unknown"})')
