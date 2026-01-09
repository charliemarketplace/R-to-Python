"""
EXERCISE 1: Scatter Plots with Plotly Express

R (ggplot2) vs Python (plotly):
    R:      ggplot(df, aes(x, y, color=grp)) + geom_point()
    Python: px.scatter(df, x="x", y="y", color="grp")

plotly.express (px) is the high-level API - similar to ggplot2!

Basic scatter:
    import plotly.express as px
    fig = px.scatter(df, x="col1", y="col2")
    fig.show()

With aesthetics:
    fig = px.scatter(df,
        x="col1", y="col2",
        color="category",    # Color by column
        size="value",        # Size by column
        hover_data=["extra"] # Show on hover
    )

TASK:
Create scatter plots of the car data.
"""
import plotly.express as px
import pandas as pd

cars = pd.DataFrame({
    "mpg": [21.0, 21.0, 22.8, 21.4, 18.7, 18.1, 14.3, 24.4, 22.8, 19.2],
    "horsepower": [110, 110, 93, 110, 175, 105, 245, 62, 95, 123],
    "weight": [2620, 2875, 2320, 3215, 3440, 3460, 3570, 3190, 3150, 3440],
    "cylinders": [6, 6, 4, 6, 8, 6, 8, 4, 4, 6],
    "name": ["Mazda RX4", "Mazda RX4 Wag", "Datsun 710", "Hornet 4 Drive",
             "Hornet Sportabout", "Valiant", "Duster 360", "Merc 240D",
             "Merc 230", "Merc 280"]
})

# ---- YOUR CODE HERE ----
# Task 1: Simple scatter plot: mpg vs horsepower
fig1 = None

# Task 2: Scatter with color by cylinders
fig2 = None

# Task 3: Scatter with color=cylinders, size=weight, hover shows name
fig3 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Basic scatter")
    check_plot(fig1, "scatter",
               hint='px.scatter(cars, x="mpg", y="horsepower")')

    print("\nTask 2: Scatter with color")
    check_plot(fig2, "scatter",
               hint='px.scatter(cars, x="mpg", y="horsepower", color="cylinders")')

    print("\nTask 3: Scatter with multiple aesthetics")
    check_plot(fig3, "scatter",
               hint='Add size="weight", hover_data=["name"]')

    # Show the final plot
    print("\nDisplaying plot 3...")
    fig3.show()
