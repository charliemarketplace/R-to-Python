"""
EXERCISE 3: The No-Intercept Trap

THE GOTCHA:
When using the ARRAY API (not formula), there's NO automatic intercept!

    # Formula API - adds intercept automatically (like R)
    smf.ols('y ~ x', data=df).fit()

    # Array API - NO intercept by default!
    sm.OLS(y, X).fit()  # No intercept!
    sm.OLS(y, sm.add_constant(X)).fit()  # With intercept

R comparison:
    R:      lm(y ~ x)      # Has intercept
            lm(y ~ x - 1)  # No intercept (explicit)
    Python: sm.OLS(y, X)   # No intercept (sneaky!)
            smf.ols('y ~ x - 1')  # No intercept (explicit)

Why does this matter?
- Without intercept, all coefficients are biased toward 0
- Your model forces the line through the origin
- This is rarely what you want!

TASK:
1. Fit a model using array API WITHOUT intercept (to see the problem)
2. Fit correctly WITH intercept using sm.add_constant()
3. Compare the coefficients
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Simple data: y = 5 + 2*x + noise
np.random.seed(42)
x = np.random.randn(100)
y = 5 + 2 * x + np.random.randn(100) * 0.5

df = pd.DataFrame({"x": x, "y": y})

# ---- YOUR CODE HERE ----
# Task 1: Fit WITHOUT intercept using array API (WRONG way)
# This will give biased results
X_no_intercept = df[["x"]]
model_wrong = None  # sm.OLS(df["y"], X_no_intercept).fit()

# Task 2: Fit WITH intercept using add_constant (CORRECT way)
X_with_intercept = None  # Use sm.add_constant()
model_correct = None

# Task 3: Also fit using formula API (for comparison)
model_formula = None  # smf.ols('y ~ x', data=df).fit()
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Model WITHOUT intercept (wrong)")
    print(f"Coefficient: {model_wrong.params.iloc[0]:.4f}")
    print("(This is biased because no intercept!)")

    print("\nTask 2: Model WITH intercept (correct)")
    check("const" in model_correct.params.index, expected=True,
          hint="sm.add_constant(X) adds a column of 1s")
    print(f"Intercept: {model_correct.params['const']:.4f} (should be ~5)")
    print(f"Slope: {model_correct.params['x']:.4f} (should be ~2)")

    print("\nTask 3: Formula API (also correct)")
    check("Intercept" in model_formula.params.index, expected=True)

    print("\n--- Comparison ---")
    print(f"True intercept: 5, True slope: 2")
    print(f"Wrong model slope: {model_wrong.params.iloc[0]:.4f}")
    print(f"Correct model intercept: {model_correct.params['const']:.4f}")
    print(f"Correct model slope: {model_correct.params['x']:.4f}")
