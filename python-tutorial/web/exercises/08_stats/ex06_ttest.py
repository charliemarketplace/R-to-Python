"""
EXERCISE 6: T-Test with scipy.stats

R vs Python:
    R:      t.test(x, y)
            t.test(value ~ group, data=df)
    Python: stats.ttest_ind(x, y)  # Independent samples
            stats.ttest_rel(x, y)  # Paired samples
            stats.ttest_1samp(x, popmean)  # One-sample

scipy.stats provides all common hypothesis tests:

    from scipy import stats

    # Two independent samples
    t_stat, p_value = stats.ttest_ind(group1, group2)

    # Paired samples
    t_stat, p_value = stats.ttest_rel(before, after)

    # One sample vs hypothesized mean
    t_stat, p_value = stats.ttest_1samp(sample, 0)

    # Welch's t-test (unequal variances)
    t_stat, p_value = stats.ttest_ind(g1, g2, equal_var=False)

TASK:
1. Test if two groups have different means
2. Test if a sample mean differs from 100
3. Perform a paired t-test
"""
import numpy as np
from scipy import stats

np.random.seed(42)

# Two groups
group_a = np.array([105, 112, 98, 110, 108, 115, 102, 109, 111, 107])
group_b = np.array([95, 102, 88, 98, 92, 105, 90, 97, 99, 94])

# Paired data (before/after)
before = np.array([150, 140, 155, 145, 160, 148, 152, 142, 158, 144])
after = np.array([145, 135, 150, 140, 152, 142, 148, 138, 150, 140])

# ---- YOUR CODE HERE ----
# Task 1: Independent samples t-test
# Test if group_a and group_b have different means
t_stat_ind, p_value_ind = None, None

# Task 2: One-sample t-test
# Test if group_a mean differs from 100
t_stat_one, p_value_one = None, None

# Task 3: Paired t-test
# Test if there's a difference between before and after
t_stat_paired, p_value_paired = None, None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Independent samples t-test")
    expected_t, expected_p = stats.ttest_ind(group_a, group_b)
    check(abs(t_stat_ind - expected_t) < 0.01, expected=True,
          hint="stats.ttest_ind(group_a, group_b)")
    print(f"t-statistic: {t_stat_ind:.4f}, p-value: {p_value_ind:.4f}")

    print("\nTask 2: One-sample t-test")
    expected_t1, expected_p1 = stats.ttest_1samp(group_a, 100)
    check(abs(t_stat_one - expected_t1) < 0.01, expected=True,
          hint="stats.ttest_1samp(group_a, 100)")
    print(f"t-statistic: {t_stat_one:.4f}, p-value: {p_value_one:.4f}")

    print("\nTask 3: Paired t-test")
    expected_tp, expected_pp = stats.ttest_rel(before, after)
    check(abs(t_stat_paired - expected_tp) < 0.01, expected=True,
          hint="stats.ttest_rel(before, after)")
    print(f"t-statistic: {t_stat_paired:.4f}, p-value: {p_value_paired:.4f}")
