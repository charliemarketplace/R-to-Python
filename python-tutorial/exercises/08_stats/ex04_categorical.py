"""
EXERCISE 4: Categorical Variables with C()

R vs Python:
    R:      lm(y ~ factor(group))  # R auto-detects factors
    Python: smf.ols('y ~ C(group)')  # Must explicitly use C()

In Python's formula API:
- Numeric columns are treated as continuous
- String columns are auto-detected as categorical
- But it's SAFER to explicitly use C() for categorical variables

The C() wrapper:
    'y ~ C(category)'           # Basic categorical
    'y ~ C(category, Treatment("A"))'  # Set reference level

R comparison:
    R auto-converts characters to factors, but Python doesn't always
    Using C() makes your intent explicit

TASK:
Fit a model predicting salary from department (categorical).
"""
import pandas as pd
import statsmodels.formula.api as smf

employees = pd.DataFrame({
    "salary": [50000, 55000, 60000, 45000, 70000, 65000, 48000, 52000, 80000],
    "dept": ["Sales", "Sales", "Eng", "Sales", "Eng", "Eng", "HR", "HR", "Eng"],
    "years": [2, 3, 4, 1, 5, 4, 2, 3, 6]
})

# ---- YOUR CODE HERE ----
# Task 1: Fit model with dept as categorical
# salary ~ C(dept)
model_cat = None

# Task 2: Fit model with dept AND years
# salary ~ C(dept) + years
model_both = None

# Task 3: Check which department is the reference category
# (The one NOT in the coefficient names)
reference_dept = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Categorical model")
    print(model_cat.summary())
    check(hasattr(model_cat, 'params'), expected=True,
          hint="smf.ols('salary ~ C(dept)', data=employees).fit()")

    # Check that categorical encoding worked
    param_names = list(model_cat.params.index)
    has_dept_coeffs = any('dept' in p.lower() for p in param_names)
    check(has_dept_coeffs, expected=True,
          hint="Should have coefficient(s) for dept categories")

    print("\nTask 2: Model with dept and years")
    check("years" in model_both.params.index, expected=True)

    print("\nTask 3: Reference category")
    # Reference is whichever dept is NOT in coefficient names
    check(reference_dept in ["Sales", "Eng", "HR"], expected=True,
          hint="Look at which category is missing from model.params")

    print(f"\nReference department: {reference_dept}")
    print("Other dept coefficients are relative to this reference.")
