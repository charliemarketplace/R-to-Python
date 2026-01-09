"""Tests for Module 6: Pandas"""

import pytest
import pandas as pd
import numpy as np


class TestEx01DataFrameCreation:
    """Test DataFrame creation."""

    def test_from_dict(self):
        df = pd.DataFrame({
            "name": ["Alice", "Bob"],
            "age": [30, 25]
        })
        assert len(df) == 2
        assert list(df.columns) == ["name", "age"]


class TestEx02SelectingColumns:
    """Test column selection."""

    def test_select_column(self):
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})

        # Single column as Series
        assert isinstance(df["a"], pd.Series)

        # Single column as DataFrame
        assert isinstance(df[["a"]], pd.DataFrame)


class TestEx03FilteringRows:
    """Test row filtering."""

    def test_filter_rows(self):
        df = pd.DataFrame({"x": [1, 2, 3, 4, 5]})
        filtered = df[df["x"] > 3]
        assert list(filtered["x"]) == [4, 5]


class TestEx04LocIloc:
    """Test loc and iloc."""

    def test_loc_iloc(self):
        df = pd.DataFrame({"x": [10, 20, 30]}, index=["a", "b", "c"])

        assert df.iloc[0]["x"] == 10
        assert df.loc["a"]["x"] == 10


class TestEx05AddingColumns:
    """Test adding columns."""

    def test_add_column(self):
        df = pd.DataFrame({"a": [1, 2], "b": [3, 4]})
        df["c"] = df["a"] + df["b"]
        assert list(df["c"]) == [4, 6]


class TestEx06Groupby:
    """Test groupby operations."""

    def test_groupby(self):
        df = pd.DataFrame({
            "cat": ["A", "A", "B", "B"],
            "val": [1, 2, 3, 4]
        })
        result = df.groupby("cat")["val"].mean()
        assert result["A"] == 1.5
        assert result["B"] == 3.5


class TestEx07Sorting:
    """Test sorting."""

    def test_sort_values(self):
        df = pd.DataFrame({"x": [3, 1, 2]})
        sorted_df = df.sort_values("x")
        assert list(sorted_df["x"]) == [1, 2, 3]


class TestEx08MissingValues:
    """Test missing value handling."""

    def test_missing_values(self):
        df = pd.DataFrame({"x": [1, np.nan, 3]})
        assert df["x"].isna().sum() == 1
        filled = df["x"].fillna(0)
        assert list(filled) == [1.0, 0.0, 3.0]


class TestEx09Merging:
    """Test merging."""

    def test_merge(self):
        df1 = pd.DataFrame({"key": [1, 2], "val1": ["a", "b"]})
        df2 = pd.DataFrame({"key": [1, 2], "val2": ["x", "y"]})
        merged = df1.merge(df2, on="key")
        assert len(merged) == 2
        assert "val1" in merged.columns
        assert "val2" in merged.columns


class TestEx10Melt:
    """Test melt (wide to long)."""

    def test_melt(self):
        wide = pd.DataFrame({
            "id": [1, 2],
            "A": [10, 20],
            "B": [30, 40]
        })
        long = wide.melt(id_vars=["id"], var_name="var", value_name="val")
        assert len(long) == 4


class TestEx11Pivot:
    """Test pivot (long to wide)."""

    def test_pivot(self):
        long = pd.DataFrame({
            "id": [1, 1, 2, 2],
            "var": ["A", "B", "A", "B"],
            "val": [10, 20, 30, 40]
        })
        wide = long.pivot(index="id", columns="var", values="val")
        assert wide.loc[1, "A"] == 10
        assert wide.loc[2, "B"] == 40
