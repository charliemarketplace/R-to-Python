"""
EXERCISE 6: Faceting (Small Multiples)

R (ggplot2) vs Python (plotly):
    R:      ... + facet_wrap(~var)
            ... + facet_grid(row ~ col)
    Python: px.scatter(..., facet_col="var")
            px.scatter(..., facet_row="row", facet_col="col")

Faceting creates a grid of subplots:

    # Column facets
    px.scatter(df, x="x", y="y", facet_col="category")

    # Row facets
    px.scatter(df, x="x", y="y", facet_row="category")

    # Grid (row x column)
    px.scatter(df, x="x", y="y", facet_row="cat1", facet_col="cat2")

    # Wrap columns
    px.scatter(df, x="x", y="y", facet_col="category",
               facet_col_wrap=2)  # 2 columns before wrapping

TASK:
Create faceted plots.
"""
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

# Tips-like data
tips = pd.DataFrame({
    "total_bill": np.random.uniform(10, 60, 100),
    "tip": np.random.uniform(1, 10, 100),
    "day": np.random.choice(["Thur", "Fri", "Sat", "Sun"], 100),
    "time": np.random.choice(["Lunch", "Dinner"], 100),
    "size": np.random.choice([2, 3, 4, 5], 100)
})

# ---- YOUR CODE HERE ----
# Task 1: Scatter of total_bill vs tip, faceted by day (columns)
fig1 = None

# Task 2: Scatter faceted by time (rows)
fig2 = None

# Task 3: Scatter faceted by day (col) and time (row)
fig3 = None

# Task 4: Faceted by day with 2 columns per row (facet_col_wrap)
fig4 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Column facets by day")
    check_plot(fig1, "scatter",
               hint='px.scatter(tips, x="total_bill", y="tip", facet_col="day")')

    print("\nTask 2: Row facets by time")
    check_plot(fig2, "scatter",
               hint='px.scatter(..., facet_row="time")')

    print("\nTask 3: Grid facets")
    check_plot(fig3, "scatter",
               hint='px.scatter(..., facet_row="time", facet_col="day")')

    print("\nTask 4: Wrapped facets")
    check_plot(fig4, "scatter",
               hint='px.scatter(..., facet_col="day", facet_col_wrap=2)')

    print("\nDisplaying plot 3...")
    fig3.show()
