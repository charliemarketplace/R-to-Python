"""
EXERCISE 3: Dictionaries - Key-Value Pairs

R vs Python:
    R:      list(name="Alice", age=30)  # Named list
            x$name or x[["name"]]       # Access
    Python: {"name": "Alice", "age": 30}  # Dict
            x["name"]                     # Access

Python dicts are like R's named lists, but:
- Keys must be hashable (strings, numbers, tuples - NOT lists)
- Access uses [] with key, not $ or [[]]
- More methods available

Creating dicts:
    d = {"a": 1, "b": 2}          # Literal
    d = dict(a=1, b=2)            # Constructor (keys become strings)
    d = dict([("a", 1), ("b", 2)])  # From pairs

Accessing:
    d["key"]      # Raises KeyError if missing
    d.get("key")  # Returns None if missing
    d.get("key", default)  # Returns default if missing

TASK:
1. Create a dict `person` with keys "name", "age", "city"
   Values: "Alice", 30, "NYC"
2. Access the "age" value and store in `age`
3. Try to access "country" safely (should return "Unknown")
"""

# ---- YOUR CODE HERE ----
# Task 1: Create the dict
person = None

# Task 2: Get age
age = None

# Task 3: Get country safely (doesn't exist, return "Unknown")
country = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: person dict")
    check(person, expected={"name": "Alice", "age": 30, "city": "NYC"})

    print("\nTask 2: age value")
    check(age, expected=30)

    print("\nTask 3: country (safe access)")
    check(country, expected="Unknown",
          hint="Use .get('country', 'Unknown') to return default for missing key")
