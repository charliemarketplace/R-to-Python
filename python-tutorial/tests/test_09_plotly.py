"""Tests for Module 9: Plotly"""

import pytest
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class TestEx01Scatter:
    """Test scatter plots."""

    def test_scatter_creation(self):
        df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 4, 9]})
        fig = px.scatter(df, x="x", y="y")
        assert len(fig.data) > 0
        assert fig.data[0].type == "scatter"


class TestEx02Line:
    """Test line plots."""

    def test_line_creation(self):
        df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 2, 3]})
        fig = px.line(df, x="x", y="y")
        assert len(fig.data) > 0


class TestEx03Bar:
    """Test bar charts."""

    def test_bar_creation(self):
        df = pd.DataFrame({"cat": ["A", "B", "C"], "val": [1, 2, 3]})
        fig = px.bar(df, x="cat", y="val")
        assert len(fig.data) > 0
        assert fig.data[0].type == "bar"


class TestEx04Histogram:
    """Test histograms."""

    def test_histogram_creation(self):
        df = pd.DataFrame({"x": [1, 2, 2, 3, 3, 3, 4, 4, 5]})
        fig = px.histogram(df, x="x")
        assert len(fig.data) > 0
        assert fig.data[0].type == "histogram"


class TestEx05Box:
    """Test box plots."""

    def test_box_creation(self):
        df = pd.DataFrame({
            "cat": ["A", "A", "B", "B"],
            "val": [1, 2, 3, 4]
        })
        fig = px.box(df, x="cat", y="val")
        assert len(fig.data) > 0
        assert fig.data[0].type == "box"


class TestEx06Facets:
    """Test faceting."""

    def test_facet_col(self):
        df = pd.DataFrame({
            "x": [1, 2, 3, 4],
            "y": [1, 2, 3, 4],
            "cat": ["A", "A", "B", "B"]
        })
        fig = px.scatter(df, x="x", y="y", facet_col="cat")
        assert len(fig.data) > 0


class TestEx07Layout:
    """Test layout customization."""

    def test_update_layout(self):
        df = pd.DataFrame({"x": [1, 2, 3], "y": [1, 2, 3]})
        fig = px.scatter(df, x="x", y="y")
        fig.update_layout(title="Test Title", xaxis_title="X Label")

        assert fig.layout.title.text == "Test Title"
        assert fig.layout.xaxis.title.text == "X Label"


class TestEx08GraphObjects:
    """Test graph objects."""

    def test_multiple_traces(self):
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[1, 2, 3], name="line1"))
        fig.add_trace(go.Scatter(x=[1, 2, 3], y=[3, 2, 1], name="line2"))

        assert len(fig.data) == 2
