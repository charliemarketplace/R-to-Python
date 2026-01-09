"""
EXERCISE 7: Correlation Tests

R vs Python:
    R:      cor(x, y)
            cor.test(x, y)
    Python: np.corrcoef(x, y)[0, 1]  # Just correlation
            stats.pearsonr(x, y)      # With p-value
            stats.spearmanr(x, y)     # Rank correlation

scipy.stats correlation functions:

    # Pearson (linear correlation)
    r, p_value = stats.pearsonr(x, y)

    # Spearman (rank correlation)
    rho, p_value = stats.spearmanr(x, y)

    # Kendall's tau
    tau, p_value = stats.kendalltau(x, y)

NumPy for just the coefficient (no p-value):
    np.corrcoef(x, y)  # Returns 2x2 matrix

pandas correlation:
    df.corr()  # Correlation matrix
    df['a'].corr(df['b'])  # Single correlation

TASK:
Calculate various correlation measures between height and weight.
"""
import numpy as np
from scipy import stats
import pandas as pd

np.random.seed(42)

# Correlated data
height = np.array([165, 170, 175, 168, 180, 172, 178, 169, 174, 182])
weight = np.array([60, 65, 72, 62, 80, 68, 75, 64, 70, 82])

df = pd.DataFrame({"height": height, "weight": weight})

# ---- YOUR CODE HERE ----
# Task 1: Pearson correlation with p-value
pearson_r, pearson_p = None, None

# Task 2: Spearman correlation with p-value
spearman_rho, spearman_p = None, None

# Task 3: Correlation using numpy (just the coefficient)
numpy_corr = None  # Extract from np.corrcoef result

# Task 4: Correlation using pandas
pandas_corr = None  # df['height'].corr(df['weight'])
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Pearson correlation")
    expected_r, expected_p = stats.pearsonr(height, weight)
    check(abs(pearson_r - expected_r) < 0.01, expected=True,
          hint="stats.pearsonr(height, weight)")
    print(f"r = {pearson_r:.4f}, p = {pearson_p:.6f}")

    print("\nTask 2: Spearman correlation")
    expected_rho, _ = stats.spearmanr(height, weight)
    check(abs(spearman_rho - expected_rho) < 0.01, expected=True,
          hint="stats.spearmanr(height, weight)")
    print(f"rho = {spearman_rho:.4f}, p = {spearman_p:.6f}")

    print("\nTask 3: NumPy correlation")
    expected_numpy = np.corrcoef(height, weight)[0, 1]
    check(abs(numpy_corr - expected_numpy) < 0.01, expected=True,
          hint="np.corrcoef(height, weight)[0, 1]")

    print("\nTask 4: Pandas correlation")
    check(abs(pandas_corr - expected_r) < 0.01, expected=True,
          hint="df['height'].corr(df['weight'])")

    print(f"\nAll methods give r = {pearson_r:.4f}")
