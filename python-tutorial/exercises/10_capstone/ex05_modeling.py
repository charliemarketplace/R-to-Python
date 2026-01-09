"""
CAPSTONE EXERCISE 5: Statistical Modeling

Build models to understand what factors influence salary:
1. Simple regression: salary ~ tenure
2. Multiple regression: salary ~ tenure + age + rating
3. Include department as categorical variable
4. Interpret results
"""
import pandas as pd
import numpy as np
from datetime import datetime
import statsmodels.formula.api as smf
from scipy import stats

# ---- DATASET ----
np.random.seed(42)
n = 100
TODAY = datetime(2024, 6, 1)

# Create data with realistic relationships
tenure = np.random.uniform(0.5, 9, n)
age = 25 + tenure * 2 + np.random.normal(0, 5, n)
age = np.clip(age, 22, 65)
rating = np.clip(3 + np.random.normal(0, 1, n), 1, 5)
dept = np.random.choice(["Engineering", "Sales", "Marketing", "HR"], n)

# Salary has relationships with tenure, rating, and department
base_salary = 50000
salary = (base_salary +
          tenure * 3000 +  # +3k per year tenure
          rating * 2000 +  # +2k per rating point
          (dept == "Engineering") * 10000 +  # Engineering pays more
          np.random.normal(0, 5000, n))

df = pd.DataFrame({
    "salary": salary.round(2),
    "tenure_years": tenure.round(2),
    "age": age.round(0).astype(int),
    "rating": rating.round(1),
    "department": dept
})

# ---- YOUR CODE HERE ----
# Task 1: Simple regression - salary ~ tenure_years
model1 = None
tenure_coef = None  # Coefficient for tenure_years

# Task 2: Multiple regression - salary ~ tenure_years + age + rating
model2 = None
r_squared = None  # R-squared of model2

# Task 3: Full model with department - salary ~ tenure_years + rating + C(department)
model3 = None

# Task 4: Test if tenure coefficient is significantly different from 0
# Get the p-value for tenure_years from model3
tenure_pvalue = None

# Task 5: Predict salary for a new employee:
# tenure=5 years, rating=4.0, department=Engineering
new_employee = pd.DataFrame({
    "tenure_years": [5.0],
    "rating": [4.0],
    "department": ["Engineering"]
})
predicted_salary = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("=== Statistical Modeling ===\n")

    print("Task 1: Simple regression")
    check(model1 is not None and hasattr(model1, 'params'), expected=True,
          hint="smf.ols('salary ~ tenure_years', data=df).fit()")
    print(f"Tenure coefficient: {model1.params['tenure_years']:.2f}")

    print("\nTask 2: Multiple regression")
    check(model2 is not None, expected=True)
    check(r_squared is not None and 0 <= r_squared <= 1, expected=True,
          hint="model2.rsquared")
    print(f"R-squared: {r_squared:.4f}")
    print("Coefficients:")
    print(model2.params)

    print("\nTask 3: Model with categorical department")
    check(model3 is not None, expected=True,
          hint="smf.ols('salary ~ tenure_years + rating + C(department)', data=df).fit()")
    print(model3.summary().tables[1])

    print("\nTask 4: P-value for tenure")
    check(tenure_pvalue is not None, expected=True,
          hint="model3.pvalues['tenure_years']")
    print(f"Tenure p-value: {tenure_pvalue:.6f}")
    if tenure_pvalue < 0.05:
        print("Tenure is statistically significant!")

    print("\nTask 5: Prediction")
    check(predicted_salary is not None, expected=True,
          hint="model3.predict(new_employee).iloc[0]")
    print(f"Predicted salary for new employee: ${predicted_salary:,.2f}")
