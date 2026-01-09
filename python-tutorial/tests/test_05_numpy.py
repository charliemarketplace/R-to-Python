"""Tests for Module 5: NumPy"""

import pytest
import numpy as np


class TestEx01ArrayCreation:
    """Test array creation."""

    def test_array_creation(self):
        arr1 = np.array([1, 2, 3, 4, 5])
        assert list(arr1) == [1, 2, 3, 4, 5]

        arr2 = np.zeros((2, 3))
        assert arr2.shape == (2, 3)

        arr3 = np.arange(10)
        assert list(arr3) == list(range(10))

        arr4 = np.linspace(0, 1, 5)
        assert len(arr4) == 5


class TestEx02Indexing:
    """Test array indexing."""

    def test_indexing(self):
        matrix = np.array([
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ])

        assert matrix[1, 2] == 7
        assert list(matrix[1]) == [5, 6, 7, 8]
        assert list(matrix[:, 2]) == [3, 7, 11]


class TestEx03BooleanIndexing:
    """Test boolean indexing."""

    def test_boolean_indexing(self):
        scores = np.array([85, 55, 90, 70, 45])
        assert list(scores[scores > 80]) == [85, 90]
        assert (scores < 60).sum() == 2


class TestEx04Reshape:
    """Test reshaping."""

    def test_reshape(self):
        arr = np.arange(1, 13)
        mat = arr.reshape(3, 4)
        assert mat.shape == (3, 4)
        assert mat[0, 0] == 1
        assert mat[2, 3] == 12


class TestEx05Broadcasting:
    """Test broadcasting."""

    def test_broadcasting(self):
        arr = np.array([1, 2, 3])
        assert list(arr + 10) == [11, 12, 13]

        matrix = np.array([[1, 2, 3], [4, 5, 6]])
        row = np.array([10, 20, 30])
        result = matrix + row
        assert result[0, 0] == 11
        assert result[1, 2] == 36


class TestEx07Aggregations:
    """Test aggregations with axis."""

    def test_axis_aggregations(self):
        sales = np.array([
            [100, 120, 110, 130],
            [90, 100, 120, 140],
            [150, 140, 130, 120],
        ])

        assert sales.sum() == 1450
        assert list(sales.sum(axis=1)) == [460, 450, 540]  # Per store
        assert list(sales.sum(axis=0)) == [340, 360, 360, 390]  # Per quarter


class TestEx08VectorizedOps:
    """Test vectorized operations."""

    def test_vectorized(self):
        values = np.array([1.0, 4.0, 9.0])
        assert list(np.sqrt(values)) == [1.0, 2.0, 3.0]


class TestEx09ViewsCopies:
    """Test views vs copies."""

    def test_slice_is_view(self):
        original = np.array([1, 2, 3, 4, 5])
        view = original[1:4]
        assert np.shares_memory(original, view)

        copy = original[1:4].copy()
        assert not np.shares_memory(original, copy)
