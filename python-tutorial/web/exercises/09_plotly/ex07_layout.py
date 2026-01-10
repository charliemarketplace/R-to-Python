"""
EXERCISE 7: Customizing Layouts

R (ggplot2) vs Python (plotly):
    R:      ... + labs(title="Title", x="X", y="Y") + theme_minimal()
    Python: fig.update_layout(title="Title", xaxis_title="X", yaxis_title="Y")

Layout customization:

    fig.update_layout(
        title="Main Title",
        title_x=0.5,  # Center title
        xaxis_title="X Axis Label",
        yaxis_title="Y Axis Label",
        template="plotly_white",  # Theme
        showlegend=True,
        legend_title_text="Legend"
    )

Available templates:
    "plotly", "plotly_white", "plotly_dark",
    "ggplot2", "seaborn", "simple_white"

Direct in px:
    px.scatter(df, ..., title="Title",
               labels={"col": "Nice Label"})

TASK:
Create a well-labeled, styled plot.
"""
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)

cars = pd.DataFrame({
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2],
    "horsepower": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123],
    "cylinders": [6, 6, 4, 6, 8, 6, 8, 4, 4, 6]
})

# ---- YOUR CODE HERE ----
# Task 1: Create scatter with title and axis labels using px arguments
fig1 = None  # Use title=, labels={} in px.scatter

# Task 2: Create same plot, then customize with update_layout
fig2 = px.scatter(cars, x="mpg", y="horsepower", color="cylinders")
# Add: title (centered), axis titles, template="plotly_white"

# Task 3: Create plot with legend title customized
fig3 = px.scatter(cars, x="mpg", y="horsepower", color="cylinders")
# Customize legend title to "Number of Cylinders"

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Plot with labels")
    check_plot(fig1, "scatter",
               hint='px.scatter(..., title="...", labels={"mpg": "Miles per Gallon"})')

    print("\nTask 2: Plot with update_layout")
    check_plot(fig2, "scatter",
               hint='fig.update_layout(title="...", xaxis_title="...", template="plotly_white")')

    print("\nTask 3: Plot with legend title")
    check_plot(fig3, "scatter",
               hint='fig.update_layout(legend_title_text="...")')

    print("\nDisplaying styled plot...")
    fig2.show()
