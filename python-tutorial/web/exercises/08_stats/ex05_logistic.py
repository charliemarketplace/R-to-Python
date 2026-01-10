"""
EXERCISE 5: Logistic Regression

R vs Python:
    R:      glm(y ~ x, family=binomial, data=df)
    Python: smf.glm('y ~ x', data=df, family=sm.families.Binomial()).fit()
            # OR simpler:
            smf.logit('y ~ x', data=df).fit()

Two ways to fit logistic regression:
    1. smf.glm() with Binomial family (flexible, like R's glm)
    2. smf.logit() (convenience function for logistic)

Interpreting coefficients:
- Coefficients are log-odds ratios
- exp(coef) gives the odds ratio
- Use model.summary() for full output

Getting predictions:
    model.predict(new_data)  # Predicted probabilities

TASK:
Fit a logistic regression predicting survival from age and fare.
"""
import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Simplified Titanic-like data
passengers = pd.DataFrame({
    "survived": [1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0],
    "age": [22, 38, 26, 35, 28, 2, 27, 14, 4, 58, 30, 45, 40, 19, 31],
    "fare": [7.25, 71.28, 7.92, 53.1, 8.46, 21.08, 11.13, 30.07, 16.7, 26.55,
             8.05, 35.5, 7.85, 30.0, 7.73],
    "pclass": [3, 1, 3, 1, 3, 3, 3, 2, 3, 1, 3, 2, 3, 2, 3]
})

# ---- YOUR CODE HERE ----
# Task 1: Fit logistic regression: survived ~ age + fare
# Use smf.logit() or smf.glm() with Binomial family
model = None

# Task 2: Get the coefficient for age
age_coef = None

# Task 3: Calculate the odds ratio for fare
# odds_ratio = exp(coefficient)
fare_odds_ratio = None

# Task 4: Get predicted probability of survival for:
# a 25 year old with fare of $50
new_passenger = pd.DataFrame({"age": [25], "fare": [50]})
pred_prob = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Logistic model fitted")
    print(model.summary())
    check(hasattr(model, 'params'), expected=True,
          hint="smf.logit('survived ~ age + fare', data=passengers).fit()")

    print("\nTask 2: Age coefficient")
    check(age_coef is not None, expected=True,
          hint="model.params['age']")

    print("\nTask 3: Fare odds ratio")
    expected_or = np.exp(model.params['fare'])
    check(abs(fare_odds_ratio - expected_or) < 0.01, expected=True,
          hint="np.exp(model.params['fare'])")

    print("\nTask 4: Predicted probability")
    check(pred_prob is not None and 0 <= pred_prob <= 1, expected=True,
          hint="model.predict(new_passenger).iloc[0]")
    print(f"Predicted survival probability: {pred_prob:.3f}")
