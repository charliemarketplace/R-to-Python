"""
EXERCISE 5: Box Plots and Violin Plots

R (ggplot2) vs Python (plotly):
    R:      ggplot(df, aes(x, y)) + geom_boxplot()
    Python: px.box(df, x="x", y="y")

Box plot options:
    px.box(df, x="category", y="value")
    px.box(df, x="category", y="value", color="group")
    px.box(df, x="category", y="value", points="all")  # Show all points

Violin plots:
    px.violin(df, x="category", y="value")
    px.violin(df, x="category", y="value", box=True)  # With box inside

TASK:
Create box plots comparing salary distributions.
"""
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

salaries = pd.DataFrame({
    "salary": np.concatenate([
        np.random.normal(70000, 10000, 50),   # Sales
        np.random.normal(85000, 15000, 50),   # Engineering
        np.random.normal(75000, 8000, 50)     # Marketing
    ]),
    "dept": ["Sales"]*50 + ["Engineering"]*50 + ["Marketing"]*50,
    "level": np.random.choice(["Junior", "Senior"], 150)
})

# ---- YOUR CODE HERE ----
# Task 1: Box plot by department
fig1 = None

# Task 2: Box plot with all points shown
fig2 = None

# Task 3: Box plot colored by level
fig3 = None

# Task 4: Violin plot with box inside
fig4 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Basic box plot")
    check_plot(fig1, "box",
               hint='px.box(salaries, x="dept", y="salary")')

    print("\nTask 2: Box with points")
    check_plot(fig2, "box",
               hint='px.box(..., points="all")')

    print("\nTask 3: Box colored by level")
    check_plot(fig3, "box",
               hint='px.box(..., color="level")')

    print("\nTask 4: Violin plot")
    check_plot(fig4, "violin",
               hint='px.violin(salaries, x="dept", y="salary", box=True)')

    print("\nDisplaying plot 4...")
    fig4.show()
