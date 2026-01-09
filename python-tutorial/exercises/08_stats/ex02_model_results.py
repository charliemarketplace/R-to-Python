"""
EXERCISE 2: Accessing Model Results

R vs Python:
    R:      coef(model), summary(model)$r.squared, confint(model)
    Python: model.params, model.rsquared, model.conf_int()

Key result attributes:
    model.params        # Coefficients (like R's coef())
    model.pvalues       # p-values for coefficients
    model.rsquared      # R-squared
    model.rsquared_adj  # Adjusted R-squared
    model.fvalue        # F-statistic
    model.f_pvalue      # F-test p-value
    model.bse           # Standard errors
    model.conf_int()    # Confidence intervals (returns DataFrame)
    model.summary()     # Full summary (like R's summary())

Accessing specific coefficients:
    model.params['x1']       # Coefficient for x1
    model.pvalues['x1']      # p-value for x1

TASK:
Given a fitted model, extract various statistics.
"""
import pandas as pd
import statsmodels.formula.api as smf

# Data
cars = pd.DataFrame({
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2],
    "horsepower": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123],
    "weight": [2620, 2875, 2320, 3215, 3440, 3460, 3570, 3190, 3150, 3440]
})

# Fit model
model = smf.ols('mpg ~ horsepower + weight', data=cars).fit()

# ---- YOUR CODE HERE ----
# Task 1: Get the intercept coefficient
intercept = None

# Task 2: Get the coefficient for horsepower
hp_coef = None

# Task 3: Get the p-value for weight
weight_pval = None

# Task 4: Get R-squared
r_squared = None

# Task 5: Get 95% confidence interval for horsepower
# Returns a DataFrame - get the row for horsepower
hp_conf_int = None  # Should be a Series or array with [lower, upper]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Intercept")
    check(abs(intercept - model.params['Intercept']) < 0.001, expected=True,
          hint="model.params['Intercept']")

    print("\nTask 2: Horsepower coefficient")
    check(abs(hp_coef - model.params['horsepower']) < 0.001, expected=True,
          hint="model.params['horsepower']")

    print("\nTask 3: Weight p-value")
    check(weight_pval is not None, expected=True,
          hint="model.pvalues['weight']")

    print("\nTask 4: R-squared")
    check(r_squared is not None and 0 <= r_squared <= 1, expected=True,
          hint="model.rsquared")

    print("\nTask 5: Confidence interval for horsepower")
    check(len(hp_conf_int) == 2, expected=True,
          hint="model.conf_int().loc['horsepower']")

    print("\n--- Model Coefficients ---")
    print(model.params)
    print(f"\nR-squared: {model.rsquared:.4f}")
