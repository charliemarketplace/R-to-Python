"""Tests for Module 4: Data Structures"""

import pytest
import copy


class TestEx01Lists:
    """Test list operations."""

    def test_list_operations(self):
        numbers = [1, 2, 3, 4, 5]
        numbers.append(6)
        numbers.insert(0, 0)
        numbers.remove(3)
        popped = numbers.pop()
        assert numbers == [0, 1, 2, 4, 5]
        assert popped == 6


class TestEx02Tuples:
    """Test tuple operations."""

    def test_tuple_unpacking(self):
        rgb = (255, 128, 0)
        red, green, blue = rgb
        assert red == 255
        assert green == 128
        assert blue == 0

    def test_single_element_tuple(self):
        single = (42,)
        assert isinstance(single, tuple)
        assert len(single) == 1


class TestEx03DictsBasics:
    """Test dict creation and access."""

    def test_dict_creation(self):
        person = {"name": "Alice", "age": 30, "city": "NYC"}
        assert person["age"] == 30
        assert person.get("country", "Unknown") == "Unknown"


class TestEx04DictMethods:
    """Test dict methods."""

    def test_dict_methods(self):
        scores = {"Alice": 85, "Bob": 92, "Carol": 78}
        assert set(scores.keys()) == {"Alice", "Bob", "Carol"}
        assert set(scores.values()) == {85, 92, 78}
        assert sum(scores.values()) / len(scores) == 85.0


class TestEx05Sets:
    """Test set operations."""

    def test_set_operations(self):
        class_a = {"Alice", "Bob", "Carol", "Dave"}
        class_b = {"Carol", "Dave", "Eve", "Frank"}

        assert class_a & class_b == {"Carol", "Dave"}
        assert class_a | class_b == {"Alice", "Bob", "Carol", "Dave", "Eve", "Frank"}
        assert class_a - class_b == {"Alice", "Bob"}
        assert class_a ^ class_b == {"Alice", "Bob", "Eve", "Frank"}


class TestEx06ListOfDicts:
    """Test list of dicts (records)."""

    def test_list_of_dicts(self):
        employees = [
            {"name": "Alice", "dept": "Engineering", "salary": 95000},
            {"name": "Bob", "dept": "Marketing", "salary": 75000},
            {"name": "Carol", "dept": "Engineering", "salary": 105000},
        ]

        assert employees[0]["name"] == "Alice"
        salaries = [e["salary"] for e in employees]
        assert salaries == [95000, 75000, 105000]


class TestEx07DictOfLists:
    """Test dict of lists (columnar)."""

    def test_dict_of_lists(self):
        employees = [
            {"name": "Alice", "salary": 95000},
            {"name": "Bob", "salary": 75000},
        ]

        columns = {
            k: [r[k] for r in employees]
            for k in employees[0].keys()
        }

        assert columns["name"] == ["Alice", "Bob"]
        assert columns["salary"] == [95000, 75000]


class TestEx09SafeNestedAccess:
    """Test safe nested access."""

    def test_safe_access(self):
        users = {"user1": {"address": {"city": "NYC"}}}

        city = users.get("user1", {}).get("address", {}).get("city", "Unknown")
        assert city == "NYC"

        missing = users.get("user2", {}).get("address", {}).get("city", "Unknown")
        assert missing == "Unknown"


class TestEx10DeepCopy:
    """Test deep vs shallow copy."""

    def test_deep_copy(self):
        original = {"scores": [1, 2, 3]}
        shallow = original.copy()
        deep = copy.deepcopy(original)

        shallow["scores"].append(4)
        assert 4 in original["scores"]  # Shallow copy shares inner list

        deep["scores"].append(5)
        assert 5 not in original["scores"]  # Deep copy is independent
