"""Tests for Module 2: Control Flow"""

import pytest


class TestEx01ForLoops:
    """Test for loop basics."""

    def test_celsius_conversion(self):
        fahrenheit = [32, 68, 77, 98.6, 212]
        celsius = [(f - 32) * 5 / 9 for f in fahrenheit]
        expected = [0.0, 20.0, 25.0, 37.0, 100.0]
        for c, e in zip(celsius, expected):
            assert abs(c - e) < 0.1


class TestEx02Range:
    """Test range function."""

    def test_range_10(self):
        assert list(range(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_range_1_11(self):
        assert list(range(1, 11)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def test_range_step(self):
        assert list(range(2, 21, 2)) == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


class TestEx03Enumerate:
    """Test enumerate function."""

    def test_enumerate_with_start(self):
        fruits = ['apple', 'banana', 'cherry', 'date']
        result = {fruit: i for i, fruit in enumerate(fruits, start=1)}
        assert result == {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}


class TestEx04Zip:
    """Test zip function."""

    def test_zip_to_dict(self):
        names = ['Alice', 'Bob', 'Carol', 'Dave']
        scores = [85, 92, 78, 95]
        result = dict(zip(names, scores))
        assert result == {'Alice': 85, 'Bob': 92, 'Carol': 78, 'Dave': 95}


class TestEx05WhileLoops:
    """Test while loops."""

    def test_gauss_sum(self):
        total = 0
        n = 1
        while n <= 100:
            total += n
            n += 1
        assert total == 5050


class TestEx06ListComprehension:
    """Test list comprehensions."""

    def test_squares(self):
        squares = [x**2 for x in range(1, 11)]
        assert squares == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    def test_filter_evens(self):
        evens = [x for x in range(1, 21) if x % 2 == 0]
        assert evens == [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


class TestEx07DictComprehension:
    """Test dict comprehensions."""

    def test_cubes(self):
        cubes = {x: x**3 for x in range(1, 6)}
        assert cubes == {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}


class TestEx08ConditionalExpression:
    """Test ternary operator."""

    def test_ternary(self):
        score = 75
        category = "high" if score >= 80 else "low"
        assert category == "low"


class TestEx09TryExcept:
    """Test exception handling."""

    def test_safe_divide(self):
        def safe_divide(a, b):
            try:
                return a / b
            except (ZeroDivisionError, TypeError):
                return None

        assert safe_divide(10, 2) == 5.0
        assert safe_divide(5, 0) is None
        assert safe_divide('a', 2) is None


class TestEx10ClosureTrap:
    """Test late binding closure fix."""

    def test_multipliers(self):
        # Fixed version
        multipliers = [lambda x, i=i: x * i for i in range(5)]
        results = [f(10) for f in multipliers]
        assert results == [0, 10, 20, 30, 40]
