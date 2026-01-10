"""
EXERCISE 3: Bar Charts

R (ggplot2) vs Python (plotly):
    R:      ggplot(df, aes(x, y)) + geom_bar(stat="identity")
            ggplot(df, aes(x)) + geom_bar()  # counts
    Python: px.bar(df, x="x", y="y")  # values
            px.histogram(df, x="x")   # counts

Bar chart types:
    px.bar(df, x="category", y="value")     # Vertical bars
    px.bar(df, x="value", y="category",     # Horizontal bars
           orientation="h")

Grouped/stacked:
    px.bar(df, x="x", y="y", color="group")  # Grouped (default)
    px.bar(df, x="x", y="y", color="group",
           barmode="stack")                   # Stacked

TASK:
Create bar charts showing sales data.
"""
import plotly.express as px
import pandas as pd

sales = pd.DataFrame({
    "product": ["Widget", "Gadget", "Gizmo", "Widget", "Gadget", "Gizmo"],
    "quarter": ["Q1", "Q1", "Q1", "Q2", "Q2", "Q2"],
    "revenue": [100, 150, 80, 120, 140, 90]
})

# Summary data
product_totals = sales.groupby("product")["revenue"].sum().reset_index()

# ---- YOUR CODE HERE ----
# Task 1: Simple bar chart of product totals
fig1 = None

# Task 2: Grouped bar chart (products by quarter)
fig2 = None

# Task 3: Stacked bar chart
fig3 = None

# Task 4: Horizontal bar chart
fig4 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Simple bar")
    check_plot(fig1, "bar",
               hint='px.bar(product_totals, x="product", y="revenue")')

    print("\nTask 2: Grouped bar")
    check_plot(fig2, "bar",
               hint='px.bar(sales, x="product", y="revenue", color="quarter")')

    print("\nTask 3: Stacked bar")
    check_plot(fig3, "bar",
               hint='Add barmode="stack"')

    print("\nTask 4: Horizontal bar")
    check_plot(fig4, "bar",
               hint='px.bar(..., orientation="h")')

    print("\nDisplaying plot 2...")
    fig2.show()
