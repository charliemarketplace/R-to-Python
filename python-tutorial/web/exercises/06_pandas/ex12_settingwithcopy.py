"""
EXERCISE 12: The SettingWithCopyWarning Trap

THE GOTCHA:
    df_subset = df[df["A"] > 0]
    df_subset["B"] = 99  # SettingWithCopyWarning!

Why? df_subset might be a VIEW of df, so changes might (or might not!)
affect the original. pandas warns because the behavior is ambiguous.

THE FIX - use .copy():
    df_subset = df[df["A"] > 0].copy()  # Explicit copy
    df_subset["B"] = 99  # Safe! No warning, no side effects

Another gotcha - chained indexing:
    df["A"]["B"] = value  # BAD! Unpredictable
    df.loc[row, "B"] = value  # GOOD! Use .loc

When to use .copy():
    1. After filtering: df[condition].copy()
    2. After slicing: df[["col1", "col2"]].copy()
    3. Anytime you want to modify a subset independently

R comparison:
    R's copy-on-modify semantics usually "just work"
    Python requires explicit awareness of views vs copies

TASK:
Fix the buggy code that causes SettingWithCopyWarning.
"""
import pandas as pd

df = pd.DataFrame({
    "category": ["A", "B", "A", "B", "A"],
    "value": [10, 20, 30, 40, 50],
    "flag": [False, False, False, False, False]
})

# ---- YOUR CODE HERE ----
# BUGGY CODE - Fix this!
# This will raise SettingWithCopyWarning:

# Task 1: Select category A rows and set their flag to True
# BUG: This is a view, not a copy
category_a = df[df["category"] == "A"]  # FIX THIS LINE
category_a["flag"] = True  # This line will warn

# Task 2: Get the high_value subset and add a new column
# BUG: This is also a view
high_value = df[df["value"] > 25]  # FIX THIS LINE
high_value["label"] = "high"  # This line will warn

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    import warnings

    # Check that modifications were isolated (didn't affect original)
    print("Task 1: category_a is independent copy")

    # If properly copied, original df should be unchanged
    # But category_a should have flag=True
    check(all(category_a["flag"] == True), expected=True,
          hint="After .copy(), you can safely modify")

    # Original should be unchanged (if you used copy correctly)
    # Note: Without copy, this test is unpredictable!

    print("\nTask 2: high_value is independent copy")
    check("label" in high_value.columns, expected=True,
          hint="Add .copy() after the filter: df[condition].copy()")
    check(all(high_value["label"] == "high"), expected=True)

    print("\nKey lesson: Use .copy() after filtering to avoid warnings and bugs!")
    print('  df_subset = df[df["A"] > 0].copy()')
