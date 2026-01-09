"""
EXERCISE 8: Chi-Squared Test

R vs Python:
    R:      chisq.test(table)
    Python: stats.chi2_contingency(table)

Chi-squared test for independence:

    from scipy import stats

    # Create contingency table
    observed = [[30, 10],
                [20, 40]]

    chi2, p_value, dof, expected = stats.chi2_contingency(observed)

Returns:
    chi2     - Chi-squared statistic
    p_value  - p-value
    dof      - Degrees of freedom
    expected - Expected frequencies under null hypothesis

Creating contingency tables from data:
    pd.crosstab(df['var1'], df['var2'])

TASK:
Test if there's an association between treatment and outcome.
"""
import numpy as np
import pandas as pd
from scipy import stats

# Observed data: Treatment vs Outcome
# Rows: Treatment (A, B), Columns: Outcome (Success, Failure)
observed = np.array([
    [45, 15],   # Treatment A: 45 success, 15 failure
    [30, 30]    # Treatment B: 30 success, 30 failure
])

# Also test from raw data
raw_data = pd.DataFrame({
    "treatment": ["A"]*60 + ["B"]*60,
    "outcome": (["Success"]*45 + ["Failure"]*15 +
                ["Success"]*30 + ["Failure"]*30)
})

# ---- YOUR CODE HERE ----
# Task 1: Chi-squared test on the observed array
chi2, p_value, dof, expected = None, None, None, None

# Task 2: Create contingency table from raw_data using pd.crosstab
contingency_table = None

# Task 3: Chi-squared test on contingency table
chi2_from_df, p_from_df, _, _ = None, None, None, None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Chi-squared test")
    exp_chi2, exp_p, exp_dof, exp_expected = stats.chi2_contingency(observed)
    check(abs(chi2 - exp_chi2) < 0.01, expected=True,
          hint="stats.chi2_contingency(observed)")
    print(f"Chi2 = {chi2:.4f}, p = {p_value:.6f}, dof = {dof}")

    print("\nTask 2: Contingency table")
    check(contingency_table is not None, expected=True,
          hint='pd.crosstab(raw_data["treatment"], raw_data["outcome"])')
    print(contingency_table)

    print("\nTask 3: Chi-squared from DataFrame")
    check(chi2_from_df is not None, expected=True,
          hint="stats.chi2_contingency(contingency_table)")

    print("\nExpected frequencies under null hypothesis:")
    print(expected)

    if p_value < 0.05:
        print(f"\np = {p_value:.4f} < 0.05: Significant association!")
    else:
        print(f"\np = {p_value:.4f} >= 0.05: No significant association")
