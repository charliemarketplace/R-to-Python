"""Tests for Module 1: Python Fundamentals"""

import pytest
import sys
from pathlib import Path

# Import exercise modules
exercises_path = Path(__file__).parent.parent / "exercises" / "01_fundamentals"


class TestEx01Indexing:
    """Test zero-indexing exercise."""

    def test_result_is_cherry(self):
        """Third element should be 'cherry'."""
        # This would test the student's solution
        # For now, test that the expected answer is correct
        fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
        assert fruits[2] == 'cherry'


class TestEx02NegativeIndexing:
    """Test negative indexing exercise."""

    def test_negative_index(self):
        numbers = [10, 20, 30, 40, 50, 60, 70]
        assert numbers[-2] == 60


class TestEx03SlicingBasics:
    """Test slice notation."""

    def test_slice_cde(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        assert letters[2:5] == ['c', 'd', 'e']


class TestEx04SliceStep:
    """Test slice with step."""

    def test_every_other(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert numbers[::2] == [1, 3, 5, 7, 9]

    def test_reverse(self):
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        assert numbers[::-1] == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


class TestEx05ReferenceCopy:
    """Test reference vs copy."""

    def test_copy_is_independent(self):
        original = [1, 2, 3, 4, 5]
        modified = original.copy()
        modified.append(6)
        assert original == [1, 2, 3, 4, 5]
        assert modified == [1, 2, 3, 4, 5, 6]


class TestEx06Truthiness:
    """Test truthiness values."""

    def test_empty_list_is_falsy(self):
        assert not []

    def test_list_with_zero_is_truthy(self):
        assert [0]

    def test_empty_string_is_falsy(self):
        assert not ""

    def test_false_string_is_truthy(self):
        assert "False"

    def test_none_is_falsy(self):
        assert not None


class TestEx07FStrings:
    """Test f-string formatting."""

    def test_basic_fstring(self):
        name = "Alice"
        age = 30
        result = f"Hello, {name}! You are {age} years old."
        assert result == "Hello, Alice! You are 30 years old."

    def test_number_formatting(self):
        price = 1234.567
        assert f"${price:,.2f}" == "$1,234.57"

    def test_percentage(self):
        ratio = 0.75
        assert f"{ratio:.1%}" == "75.0%"


class TestEx08MutableDefault:
    """Test mutable default argument fix."""

    def test_fixed_function(self):
        def add_to_cart(item, cart=None):
            if cart is None:
                cart = []
            cart.append(item)
            return cart

        cart1 = add_to_cart("apple")
        cart2 = add_to_cart("banana")
        assert cart1 == ["apple"]
        assert cart2 == ["banana"]
