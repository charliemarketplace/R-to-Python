"""
EXERCISE 10: Practical Statistical Analysis

Putting it all together: A complete statistical analysis workflow.

SCENARIO:
A company ran an A/B test on their website. They want to know:
1. Is there a difference in conversion rates between variants?
2. Is there a difference in revenue per user?
3. Build a model predicting revenue from user characteristics

TASK:
Perform a complete analysis using the techniques learned.
"""
import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf

np.random.seed(42)

# A/B test data
n_users = 200
data = pd.DataFrame({
    "user_id": range(n_users),
    "variant": np.random.choice(["A", "B"], n_users),
    "age": np.random.randint(18, 65, n_users),
    "days_since_signup": np.random.randint(1, 365, n_users),
    "converted": np.random.binomial(1, 0.3, n_users),
})

# Revenue is higher for variant B and correlates with age
data["revenue"] = (
    5 +
    (data["variant"] == "B").astype(int) * 3 +
    data["age"] * 0.1 +
    data["converted"] * 10 +
    np.random.randn(n_users) * 5
)
data.loc[data["revenue"] < 0, "revenue"] = 0

# ---- YOUR CODE HERE ----
# Task 1: Calculate conversion rate for each variant
variant_a_data = data[data["variant"] == "A"]
variant_b_data = data[data["variant"] == "B"]

conv_rate_a = None  # Proportion converted in variant A
conv_rate_b = None  # Proportion converted in variant B

# Task 2: Chi-squared test for conversion rate difference
# Create contingency table: rows=variant, cols=converted(0/1)
contingency = None  # pd.crosstab(...)
chi2, p_chi2, _, _ = None, None, None, None

# Task 3: T-test for revenue difference
revenue_a = variant_a_data["revenue"]
revenue_b = variant_b_data["revenue"]
t_stat, p_ttest = None, None

# Task 4: Linear regression: revenue ~ C(variant) + age + converted
revenue_model = None

# Task 5: Get the coefficient for variant B
# (Shows the lift from being in variant B, controlling for other factors)
variant_b_effect = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== A/B Test Analysis ===\n")

    print("Task 1: Conversion Rates")
    expected_a = variant_a_data["converted"].mean()
    expected_b = variant_b_data["converted"].mean()
    check(abs(conv_rate_a - expected_a) < 0.01, expected=True,
          hint="variant_a_data['converted'].mean()")
    print(f"Variant A: {conv_rate_a:.1%}")
    print(f"Variant B: {conv_rate_b:.1%}")

    print("\nTask 2: Chi-squared test for conversion")
    check(chi2 is not None, expected=True,
          hint="pd.crosstab(...), stats.chi2_contingency(...)")
    print(f"Chi2 = {chi2:.4f}, p = {p_chi2:.4f}")
    if p_chi2 < 0.05:
        print("Significant difference in conversion rates!")
    else:
        print("No significant difference in conversion rates")

    print("\nTask 3: T-test for revenue")
    check(t_stat is not None, expected=True,
          hint="stats.ttest_ind(revenue_a, revenue_b)")
    print(f"t = {t_stat:.4f}, p = {p_ttest:.4f}")
    print(f"Mean revenue A: ${revenue_a.mean():.2f}")
    print(f"Mean revenue B: ${revenue_b.mean():.2f}")

    print("\nTask 4: Linear model for revenue")
    check(hasattr(revenue_model, 'params'), expected=True)
    print(revenue_model.summary().tables[1])

    print("\nTask 5: Variant B effect (controlling for age, conversion)")
    check(variant_b_effect is not None, expected=True,
          hint="Look for coefficient with 'variant' and 'B' in name")
    print(f"Variant B lift: ${variant_b_effect:.2f}")

    print("\n=== Analysis Complete ===")
