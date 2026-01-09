"""
EXERCISE 4: Histograms

R (ggplot2) vs Python (plotly):
    R:      ggplot(df, aes(x)) + geom_histogram(bins=30)
    Python: px.histogram(df, x="x", nbins=30)

Histogram options:
    px.histogram(df, x="col", nbins=30)        # Set number of bins
    px.histogram(df, x="col", color="group")   # Overlaid by group
    px.histogram(df, x="col", color="group",
                 barmode="overlay", opacity=0.7)  # Semi-transparent overlay
    px.histogram(df, x="col", marginal="box")  # Add marginal box plot

TASK:
Create histograms of test score distributions.
"""
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

scores = pd.DataFrame({
    "score": np.concatenate([
        np.random.normal(75, 10, 100),  # Class A
        np.random.normal(80, 8, 100)    # Class B
    ]),
    "class": ["A"] * 100 + ["B"] * 100
})

# ---- YOUR CODE HERE ----
# Task 1: Simple histogram of all scores
fig1 = None

# Task 2: Histogram with 20 bins
fig2 = None

# Task 3: Overlaid histograms by class (semi-transparent)
fig3 = None

# Task 4: Histogram with marginal box plot
fig4 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Simple histogram")
    check_plot(fig1, "histogram",
               hint='px.histogram(scores, x="score")')

    print("\nTask 2: Histogram with nbins")
    check_plot(fig2, "histogram",
               hint='px.histogram(scores, x="score", nbins=20)')

    print("\nTask 3: Overlaid by class")
    check_plot(fig3, "histogram",
               hint='px.histogram(..., color="class", barmode="overlay", opacity=0.7)')

    print("\nTask 4: With marginal box")
    check_plot(fig4, "histogram",
               hint='px.histogram(..., marginal="box")')

    print("\nDisplaying plot 3...")
    fig3.show()
