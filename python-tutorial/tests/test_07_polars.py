"""Tests for Module 7: Polars"""

import pytest
import polars as pl


class TestEx01DataFrameCreation:
    """Test DataFrame creation."""

    def test_from_dict(self):
        df = pl.DataFrame({
            "name": ["Alice", "Bob"],
            "age": [30, 25]
        })
        assert df.height == 2
        assert df.width == 2


class TestEx02Selecting:
    """Test column selection."""

    def test_select(self):
        df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
        result = df.select("a")
        assert result.columns == ["a"]


class TestEx03Filtering:
    """Test row filtering."""

    def test_filter(self):
        df = pl.DataFrame({"x": [1, 2, 3, 4, 5]})
        filtered = df.filter(pl.col("x") > 3)
        assert filtered["x"].to_list() == [4, 5]


class TestEx04WithColumns:
    """Test adding columns."""

    def test_with_columns(self):
        df = pl.DataFrame({"a": [1, 2], "b": [3, 4]})
        result = df.with_columns(
            (pl.col("a") + pl.col("b")).alias("c")
        )
        assert result["c"].to_list() == [4, 6]


class TestEx05Expressions:
    """Test expressions."""

    def test_mean_expression(self):
        df = pl.DataFrame({"x": [1, 2, 3, 4, 5]})
        mean = df.select(pl.col("x").mean()).item()
        assert mean == 3.0


class TestEx06Groupby:
    """Test groupby."""

    def test_group_by(self):
        df = pl.DataFrame({
            "cat": ["A", "A", "B", "B"],
            "val": [1, 2, 3, 4]
        })
        result = df.group_by("cat").agg(pl.col("val").mean())
        result_dict = {row["cat"]: row["val"] for row in result.to_dicts()}
        assert result_dict["A"] == 1.5
        assert result_dict["B"] == 3.5


class TestEx07Sorting:
    """Test sorting."""

    def test_sort(self):
        df = pl.DataFrame({"x": [3, 1, 2]})
        sorted_df = df.sort("x")
        assert sorted_df["x"].to_list() == [1, 2, 3]


class TestEx08Nulls:
    """Test null handling."""

    def test_null_handling(self):
        df = pl.DataFrame({"x": [1, None, 3]})
        assert df.null_count()["x"][0] == 1

        filled = df.with_columns(pl.col("x").fill_null(0))
        assert filled["x"].to_list() == [1, 0, 3]


class TestEx09Lazy:
    """Test lazy evaluation."""

    def test_lazy(self):
        df = pl.DataFrame({"x": [1, 2, 3]})
        lazy = df.lazy()
        assert str(type(lazy).__name__) == "LazyFrame"

        result = lazy.filter(pl.col("x") > 1).collect()
        assert result["x"].to_list() == [2, 3]


class TestEx10PandasConversion:
    """Test pandas conversion."""

    def test_to_pandas(self):
        import pandas as pd

        pl_df = pl.DataFrame({"x": [1, 2, 3]})
        pd_df = pl_df.to_pandas()
        assert isinstance(pd_df, pd.DataFrame)

    def test_from_pandas(self):
        import pandas as pd

        pd_df = pd.DataFrame({"x": [1, 2, 3]})
        pl_df = pl.from_pandas(pd_df)
        assert isinstance(pl_df, pl.DataFrame)
