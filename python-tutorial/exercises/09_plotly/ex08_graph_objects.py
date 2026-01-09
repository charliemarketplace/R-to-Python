"""
EXERCISE 8: Graph Objects - Lower Level Control

plotly.express is built on plotly.graph_objects.
For full control, use graph_objects (go) directly.

    import plotly.graph_objects as go

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1,2,3], y=[1,4,9], mode='lines', name='squared'))
    fig.add_trace(go.Scatter(x=[1,2,3], y=[1,2,3], mode='markers', name='linear'))
    fig.update_layout(title="Multiple Traces")
    fig.show()

Trace types:
    go.Scatter(mode='lines')      # Line
    go.Scatter(mode='markers')    # Points
    go.Scatter(mode='lines+markers')  # Both
    go.Bar(x=[...], y=[...])
    go.Histogram(x=[...])
    go.Box(y=[...])
    go.Heatmap(z=[[...]])

When to use go vs px:
    px: Quick plots, standard visualizations
    go: Multiple traces, custom layouts, complex plots

TASK:
Create plots using graph_objects for full control.
"""
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

np.random.seed(42)
x = np.linspace(0, 10, 50)

# ---- YOUR CODE HERE ----
# Task 1: Create figure with two line traces
# Line 1: x vs sin(x), name="Sin"
# Line 2: x vs cos(x), name="Cos"
fig1 = go.Figure()
# Add traces here...

# Task 2: Create figure with bar and line on same plot
# Bar: categories A, B, C with values 10, 20, 15
# Line: same x, different y: 12, 18, 17
fig2 = go.Figure()
# Add traces here...

# Task 3: Combine a plotly express figure with additional traces
# Start with px.scatter, then add a horizontal line
df = pd.DataFrame({"x": range(10), "y": np.random.randn(10).cumsum()})
fig3 = px.scatter(df, x="x", y="y")
# Add horizontal line at y=0 using add_hline or add_trace
# Hint: fig3.add_hline(y=0, line_dash="dash")

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check_plot

    print("Task 1: Multiple line traces")
    check_plot(fig1, "scatter",
               hint="fig.add_trace(go.Scatter(x=x, y=np.sin(x), mode='lines', name='Sin'))")
    check(len(fig1.data) >= 2, expected=True,
          hint="Should have 2 traces")

    print("\nTask 2: Bar and line combined")
    has_bar = any(trace.type == 'bar' for trace in fig2.data)
    has_scatter = any(trace.type == 'scatter' for trace in fig2.data)
    check(has_bar and has_scatter, expected=True,
          hint="Add go.Bar(...) and go.Scatter(...) traces")

    print("\nTask 3: px figure with added elements")
    check_plot(fig3, "scatter")
    # Check for the horizontal line (shape or trace)
    print("Added horizontal line to scatter plot")

    print("\nDisplaying plot 1...")
    fig1.show()


# Extra import for grading
from grader.check import check
