"""Tests for Module 3: Functions"""

import pytest
import math


class TestEx01BasicFunctions:
    """Test basic function definition."""

    def test_circle_area(self):
        def circle_area(radius):
            return math.pi * radius ** 2

        assert abs(circle_area(1) - 3.14159) < 0.001
        assert abs(circle_area(2) - 12.56636) < 0.001


class TestEx02KeywordArgs:
    """Test positional and keyword arguments."""

    def test_greet_function(self):
        def greet(name, greeting, punctuation):
            return f"{greeting}, {name}{punctuation}"

        assert greet("Alice", "Hello", "!") == "Hello, Alice!"
        assert greet(name="Alice", greeting="Hello", punctuation="!") == "Hello, Alice!"
        assert greet("Alice", punctuation="!", greeting="Hello") == "Hello, Alice!"


class TestEx03DefaultArgs:
    """Test default arguments."""

    def test_power_function(self):
        def power(base, exponent=2):
            return base ** exponent

        assert power(3) == 9
        assert power(2, 3) == 8
        assert power(5, exponent=0) == 1


class TestEx04MultipleReturns:
    """Test multiple return values."""

    def test_min_max_range(self):
        def min_max_range(numbers):
            return min(numbers), max(numbers), max(numbers) - min(numbers)

        result = min_max_range([3, 1, 4, 1, 5, 9, 2, 6, 5, 3])
        assert result == (1, 9, 8)


class TestEx05Args:
    """Test *args."""

    def test_product(self):
        def product(*numbers):
            result = 1
            for n in numbers:
                result *= n
            return result

        assert product(2, 3, 4) == 24
        assert product(5) == 5
        assert product() == 1


class TestEx06Kwargs:
    """Test **kwargs."""

    def test_build_profile(self):
        def build_profile(name, **attributes):
            return {"name": name, **attributes}

        assert build_profile("Alice", age=30, city="NYC") == {
            'name': 'Alice', 'age': 30, 'city': 'NYC'
        }
        assert build_profile("Bob") == {'name': 'Bob'}


class TestEx07Scope:
    """Test variable scope."""

    def test_global_counter(self):
        call_count = 0

        def counter():
            nonlocal call_count
            call_count += 1
            return call_count

        assert counter() == 1
        assert counter() == 2
        assert counter() == 3


class TestEx08Lambda:
    """Test lambda functions."""

    def test_double(self):
        double = lambda x: x * 2
        assert double(5) == 10

    def test_sort_by_second(self):
        people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]
        sorted_people = sorted(people, key=lambda x: x[1])
        assert sorted_people == [("Bob", 25), ("Alice", 30), ("Carol", 35)]

    def test_filter_positives(self):
        numbers = [-5, 3, -2, 8, -1, 4]
        positives = list(filter(lambda x: x > 0, numbers))
        assert positives == [3, 8, 4]
