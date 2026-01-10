"""
CAPSTONE EXERCISE 6: Visualization Dashboard

Create a series of visualizations to communicate findings:
1. Salary distribution by department
2. Salary vs tenure scatter with regression line
3. Rating distribution
4. Department comparison
"""
import pandas as pd
import numpy as np
from datetime import datetime
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ---- DATASET ----
np.random.seed(42)
n = 100
TODAY = datetime(2024, 6, 1)

tenure = np.random.uniform(0.5, 9, n)
age = 25 + tenure * 2 + np.random.normal(0, 5, n)
rating = np.clip(3 + np.random.normal(0, 1, n), 1, 5)
dept = np.random.choice(["Engineering", "Sales", "Marketing", "HR"], n)
salary = (50000 + tenure * 3000 + rating * 2000 +
          (dept == "Engineering") * 10000 + np.random.normal(0, 5000, n))

df = pd.DataFrame({
    "salary": salary.round(2),
    "tenure_years": tenure.round(2),
    "age": age.round(0).astype(int),
    "rating": rating.round(1),
    "department": dept
})

# ---- YOUR CODE HERE ----
# Task 1: Box plot of salary by department
# Include all points, color by department
fig_box = None

# Task 2: Scatter plot of salary vs tenure
# Color by department, add trendline
# Hint: px.scatter(..., trendline="ols")
fig_scatter = None

# Task 3: Histogram of ratings with different colors for each department
fig_hist = None

# Task 4: Bar chart of mean salary by department
# First calculate mean salary per department
mean_by_dept = df.groupby("department")["salary"].mean().reset_index()
fig_bar = None

# Task 5: Add proper titles and labels to fig_scatter
# Title: "Salary vs Tenure by Department"
# X-axis: "Years at Company"
# Y-axis: "Annual Salary ($)"
# Use update_layout() on fig_scatter

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("=== Visualization Dashboard ===\n")

    print("Task 1: Box plot")
    check_plot(fig_box, "box",
               hint='px.box(df, x="department", y="salary", color="department", points="all")')

    print("\nTask 2: Scatter with trendline")
    check_plot(fig_scatter, "scatter",
               hint='px.scatter(df, x="tenure_years", y="salary", color="department", trendline="ols")')

    print("\nTask 3: Histogram")
    check_plot(fig_hist, "histogram",
               hint='px.histogram(df, x="rating", color="department", barmode="overlay")')

    print("\nTask 4: Bar chart")
    check_plot(fig_bar, "bar",
               hint='px.bar(mean_by_dept, x="department", y="salary")')

    print("\nTask 5: Check scatter has title")
    has_title = fig_scatter.layout.title.text is not None if fig_scatter else False
    print(f"Has title: {has_title}")

    print("\nDisplaying visualizations...")
    # Show one of the plots
    if fig_scatter:
        fig_scatter.show()
