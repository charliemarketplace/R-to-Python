"""
EXERCISE 1: Linear Regression with Formula API

R vs Python:
    R:      lm(y ~ x1 + x2, data=df)
    Python: smf.ols('y ~ x1 + x2', data=df).fit()

statsmodels has a formula API that works like R!

    import statsmodels.formula.api as smf

    model = smf.ols('y ~ x1 + x2', data=df).fit()
    print(model.summary())

Key points:
- Formula API automatically adds intercept (like R)
- Use smf.ols() for formula interface
- Must call .fit() to actually fit the model
- Results object has many useful attributes

TASK:
Fit a linear regression predicting 'mpg' from 'horsepower' and 'weight'.
"""
import pandas as pd
import statsmodels.formula.api as smf

# Car data
cars = pd.DataFrame({
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2],
    "horsepower": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123],
    "weight": [2620, 2875, 2320, 3215, 3440, 3460, 3570, 3190, 3150, 3440]
})

# ---- YOUR CODE HERE ----
# Fit linear model: mpg ~ horsepower + weight
model = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Model fitted!")
    print("\nModel summary:")
    print(model.summary())

    print("\nChecking model was fit correctly:")
    check(hasattr(model, 'params'), expected=True,
          hint="smf.ols('mpg ~ horsepower + weight', data=cars).fit()")

    # Check that we have expected parameters
    check("Intercept" in model.params.index, expected=True,
          hint="Formula API should auto-add intercept")
    check("horsepower" in model.params.index, expected=True)
    check("weight" in model.params.index, expected=True)
