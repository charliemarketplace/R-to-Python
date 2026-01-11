"""
EXERCISE 8: Nested Dicts - Hierarchical Data

R equivalent: Nested named lists
    config <- list(
        database = list(host = "localhost", port = 5432),
        api = list(timeout = 30)
    )
    config$database$host  # "localhost"

Python nested dicts:
    config = {
        "database": {"host": "localhost", "port": 5432},
        "api": {"timeout": 30}
    }
    config["database"]["host"]  # "localhost"

This is exactly how JSON/YAML config files look!

Common operations:
    # Access nested value
    value = data["level1"]["level2"]["level3"]

    # Modify nested value
    data["level1"]["level2"]["level3"] = new_value

    # Check if key exists at any level
    if "level1" in data and "level2" in data["level1"]:
        ...

TASK:
Given the config dict:
1. Get the database port
2. Get the API timeout
3. Add a new logging configuration with level="INFO" and file="app.log"
4. Change the database host to "production.db.com"
"""

config = {
    "database": {
        "host": "localhost",
        "port": 5432,
        "name": "myapp"
    },
    "api": {
        "timeout": 30,
        "retries": 3
    }
}

# ---- YOUR CODE HERE ----
# Task 1: Get database port
db_port = None

# Task 2: Get API timeout
api_timeout = None

# Task 3: Add logging config
# config["logging"] = {"level": "INFO", "file": "app.log"}

# Task 4: Change database host to "production.db.com"

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Database port")
    check(db_port, expected=5432)

    print("\nTask 2: API timeout")
    check(api_timeout, expected=30)

    print("\nTask 3: Logging config added")
    check(config.get("logging"), expected={"level": "INFO", "file": "app.log"},
          hint="config['logging'] = {'level': 'INFO', 'file': 'app.log'}")

    print("\nTask 4: Database host changed")
    check(config["database"]["host"], expected="production.db.com",
          hint="config['database']['host'] = 'production.db.com'")
