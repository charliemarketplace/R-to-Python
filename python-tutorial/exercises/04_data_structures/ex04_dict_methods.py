"""
EXERCISE 4: Dictionary Methods

Essential dict methods:
    d.keys()     # View of all keys
    d.values()   # View of all values
    d.items()    # View of (key, value) pairs
    d.update(other)  # Merge another dict into d
    d.pop(key)   # Remove key and return value

R equivalents:
    names(x)     ->  d.keys()
    unlist(x)    ->  d.values()
    -none-       ->  d.items()

Iterating over dicts:
    for key in d:              # Iterate over keys
    for key in d.keys():       # Same, explicit
    for val in d.values():     # Iterate over values
    for k, v in d.items():     # Iterate over pairs

Converting to lists:
    list(d.keys())    # ['a', 'b', 'c']
    list(d.values())  # [1, 2, 3]
    list(d.items())   # [('a', 1), ('b', 2), ('c', 3)]

TASK:
Given the scores dict:
1. Get a list of all student names (keys)
2. Get a list of all scores (values)
3. Calculate the average score
4. Add new student "Dave" with score 88 using update()
"""

scores = {"Alice": 85, "Bob": 92, "Carol": 78}

# ---- YOUR CODE HERE ----
# Task 1: List of names
names = None

# Task 2: List of scores
score_list = None

# Task 3: Average score (before adding Dave)
average = None

# Task 4: Add Dave with score 88
# (modify scores dict in place)

# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Names")
    check(sorted(names), expected=["Alice", "Bob", "Carol"],
          hint="list(scores.keys())")

    print("\nTask 2: Score list")
    check(sorted(score_list), expected=[78, 85, 92],
          hint="list(scores.values())")

    print("\nTask 3: Average score")
    check(average, expected=85.0, rtol=0.01,
          hint="sum(scores.values()) / len(scores)")

    print("\nTask 4: Dict after adding Dave")
    check(scores, expected={"Alice": 85, "Bob": 92, "Carol": 78, "Dave": 88},
          hint="scores.update({'Dave': 88}) or scores['Dave'] = 88")
