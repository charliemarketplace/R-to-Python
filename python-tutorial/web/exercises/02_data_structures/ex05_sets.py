"""
EXERCISE 5: Sets - Unique Elements

R vs Python:
    R:      unique(c(1, 2, 2, 3))  # Returns vector
    Python: set([1, 2, 2, 3])      # Returns {1, 2, 3}

Sets are:
- Unordered collections of unique elements
- Mutable (can add/remove)
- Elements must be hashable (no lists!)
- Great for membership testing, deduplication, set operations

Creating sets:
    s = {1, 2, 3}        # Literal (NOT empty dict!)
    s = set([1, 2, 3])   # From list
    s = set()            # Empty set (not {} - that's an empty dict!)

Set operations (same as R's set functions):
    a | b    # Union (a or b)
    a & b    # Intersection (a and b)
    a - b    # Difference (in a, not in b)
    a ^ b    # Symmetric difference (in one but not both)

TASK:
Given two sets of students in different classes:
1. Find students in BOTH classes (intersection)
2. Find ALL unique students (union)
3. Find students ONLY in class_a (difference)
4. Find students in exactly ONE class (symmetric difference)
"""

class_a = {"Alice", "Bob", "Carol", "Dave"}
class_b = {"Carol", "Dave", "Eve", "Frank"}

# ---- YOUR CODE HERE ----
both_classes = None      # Students in both
all_students = None      # All unique students
only_class_a = None      # Only in class_a
exactly_one = None       # In exactly one class
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Students in both classes")
    check(both_classes, expected={"Carol", "Dave"},
          hint="Use & or .intersection()")

    print("\nTask 2: All students")
    check(all_students, expected={"Alice", "Bob", "Carol", "Dave", "Eve", "Frank"},
          hint="Use | or .union()")

    print("\nTask 3: Only in class_a")
    check(only_class_a, expected={"Alice", "Bob"},
          hint="Use - or .difference()")

    print("\nTask 4: In exactly one class")
    check(exactly_one, expected={"Alice", "Bob", "Eve", "Frank"},
          hint="Use ^ or .symmetric_difference()")
