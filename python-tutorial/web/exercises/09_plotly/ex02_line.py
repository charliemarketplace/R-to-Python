"""
EXERCISE 2: Line Plots

R (ggplot2) vs Python (plotly):
    R:      ggplot(df, aes(x, y)) + geom_line()
    Python: px.line(df, x="x", y="y")

Line plots for time series or sequential data:

    fig = px.line(df, x="date", y="value")

Multiple lines:
    fig = px.line(df, x="date", y="value", color="category")

Line + markers:
    fig = px.line(df, x="date", y="value", markers=True)

TASK:
Create line plots of stock-like data.
"""
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=30, freq="D")

stocks = pd.DataFrame({
    "date": list(dates) * 2,
    "price": list(100 + np.cumsum(np.random.randn(30))) +
             list(50 + np.cumsum(np.random.randn(30) * 0.5)),
    "stock": ["AAPL"] * 30 + ["GOOG"] * 30
})

# ---- YOUR CODE HERE ----
# Task 1: Simple line plot (just AAPL)
aapl_data = stocks[stocks["stock"] == "AAPL"]
fig1 = None

# Task 2: Both stocks with color
fig2 = None

# Task 3: Both stocks with markers
fig3 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Single line")
    check_plot(fig1, "scatter",  # plotly express line creates scatter with mode='lines'
               hint='px.line(aapl_data, x="date", y="price")')

    print("\nTask 2: Multiple lines with color")
    check_plot(fig2, "scatter",
               hint='px.line(stocks, x="date", y="price", color="stock")')

    print("\nTask 3: Lines with markers")
    check_plot(fig3, "scatter",
               hint='px.line(..., markers=True)')

    print("\nDisplaying plot 3...")
    fig3.show()
