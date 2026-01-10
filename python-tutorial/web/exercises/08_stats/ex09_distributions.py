"""
EXERCISE 9: Working with Distributions

R vs Python:
    R:      pnorm(q), qnorm(p), rnorm(n), dnorm(x)
    Python: stats.norm.cdf(q), stats.norm.ppf(p), stats.norm.rvs(n), stats.norm.pdf(x)

scipy.stats distribution methods:
    dist.pdf(x)   # Probability density (dnorm)
    dist.cdf(x)   # Cumulative distribution (pnorm)
    dist.ppf(q)   # Quantile function (qnorm) - "percent point function"
    dist.rvs(n)   # Random samples (rnorm)

Common distributions:
    stats.norm    # Normal
    stats.t       # Student's t
    stats.chi2    # Chi-squared
    stats.f       # F distribution
    stats.binom   # Binomial
    stats.poisson # Poisson

Specifying parameters:
    stats.norm(loc=0, scale=1)  # mean=0, sd=1
    stats.t(df=10)              # t with 10 df
    stats.chi2(df=5)            # chi-squared with 5 df

TASK:
Work with normal and t distributions.
"""
import numpy as np
from scipy import stats

# ---- YOUR CODE HERE ----
# Task 1: Standard normal
# What is P(Z < 1.96)?
prob_z_less_196 = None  # stats.norm.cdf(1.96)

# Task 2: What z-score gives P(Z < z) = 0.975?
z_975 = None  # stats.norm.ppf(0.975)

# Task 3: Generate 1000 random samples from N(mean=100, sd=15)
np.random.seed(42)
samples = None  # stats.norm(loc=100, scale=15).rvs(1000)

# Task 4: t-distribution with 10 degrees of freedom
# What is the critical value for a two-tailed test at alpha=0.05?
# (i.e., what t gives P(T < t) = 0.975?)
t_critical = None  # stats.t(df=10).ppf(0.975)

# Task 5: Calculate the density (pdf) of standard normal at x=0
pdf_at_0 = None  # stats.norm.pdf(0)
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: P(Z < 1.96)")
    check(abs(prob_z_less_196 - 0.975) < 0.001, expected=True,
          hint="stats.norm.cdf(1.96)")
    print(f"P(Z < 1.96) = {prob_z_less_196:.4f}")

    print("\nTask 2: z for P(Z < z) = 0.975")
    check(abs(z_975 - 1.96) < 0.01, expected=True,
          hint="stats.norm.ppf(0.975)")
    print(f"z = {z_975:.4f}")

    print("\nTask 3: Random samples")
    check(len(samples) == 1000, expected=True)
    check(abs(np.mean(samples) - 100) < 5, expected=True,
          hint="stats.norm(loc=100, scale=15).rvs(1000)")
    print(f"Sample mean: {np.mean(samples):.2f}, Sample std: {np.std(samples):.2f}")

    print("\nTask 4: t critical value (df=10)")
    check(abs(t_critical - 2.228) < 0.01, expected=True,
          hint="stats.t(df=10).ppf(0.975)")
    print(f"t_critical = {t_critical:.4f}")

    print("\nTask 5: PDF at x=0")
    check(abs(pdf_at_0 - 0.3989) < 0.001, expected=True,
          hint="stats.norm.pdf(0)")
    print(f"f(0) = {pdf_at_0:.4f}")
