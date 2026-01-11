"""
EXERCISE 9: Safe Nested Access

The problem: Accessing nested data that might not exist.

    data["a"]["b"]["c"]  # KeyError if any level is missing!

Solutions:

1. Chained .get() with defaults:
    data.get("a", {}).get("b", {}).get("c", default)

2. try/except:
    try:
        value = data["a"]["b"]["c"]
    except KeyError:
        value = default

3. Check at each level (verbose):
    if "a" in data and "b" in data["a"] and "c" in data["a"]["b"]:
        value = data["a"]["b"]["c"]

The .get() chain is most Pythonic for simple cases.

R comparison:
    # R doesn't error on NULL, just returns NULL
    data$a$b$c  # NULL if missing

TASK:
Given possibly incomplete user data:
1. Safely get user1's city (exists)
2. Safely get user2's city (missing - return "Unknown")
3. Safely get user3's name (user3 doesn't exist - return "Anonymous")
"""

users = {
    "user1": {
        "name": "Alice",
        "address": {"city": "NYC", "zip": "10001"}
    },
    "user2": {
        "name": "Bob",
        "address": {}  # No city!
    }
    # user3 doesn't exist at all
}

# ---- YOUR CODE HERE ----
# Task 1: Get user1's city (should be "NYC")
city1 = None

# Task 2: Get user2's city (should return "Unknown")
city2 = None

# Task 3: Get user3's name (should return "Anonymous")
name3 = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: user1's city (exists)")
    check(city1, expected="NYC",
          hint="users['user1']['address']['city'] or chained .get()")

    print("\nTask 2: user2's city (missing)")
    check(city2, expected="Unknown",
          hint="users.get('user2', {}).get('address', {}).get('city', 'Unknown')")

    print("\nTask 3: user3's name (user missing)")
    check(name3, expected="Anonymous",
          hint="users.get('user3', {}).get('name', 'Anonymous')")
