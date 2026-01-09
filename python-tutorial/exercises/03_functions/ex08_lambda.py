"""
EXERCISE 8: Lambda Functions

R vs Python:
    R:      function(x) x^2  # Anonymous function
    Python: lambda x: x**2   # Lambda expression

Lambda functions are small, anonymous functions.
- Can only contain a single expression (no statements!)
- No `return` keyword (the expression IS the return value)
- Great for short operations, especially with map/filter/sort

    # Named function
    def square(x):
        return x ** 2

    # Equivalent lambda
    square = lambda x: x ** 2

Common uses:
    # Sort by custom key
    pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
    sorted(pairs, key=lambda x: x[1])  # Sort by second element

    # With map/filter
    list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]
    list(filter(lambda x: x > 0, [-1, 2, -3, 4]))  # [2, 4]

TASK A: Create a lambda `double` that doubles its input
TASK B: Sort the list of tuples by the second element (age)
TASK C: Filter to keep only positive numbers using filter() and lambda
"""

people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]
numbers = [-5, 3, -2, 8, -1, 4]

# ---- YOUR CODE HERE ----
# Task A: Lambda that doubles input
double = None  # lambda x: ...

# Task B: Sort people by age (second element)
sorted_by_age = None  # Use sorted() with key=lambda

# Task C: Keep only positive numbers
positives = None  # Use list(filter(lambda..., numbers))
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: double(5)")
    check(double(5), expected=10,
          hint="lambda x: x * 2")

    print("\nTask B: Sort by age")
    check(sorted_by_age, expected=[("Bob", 25), ("Alice", 30), ("Carol", 35)],
          hint="sorted(people, key=lambda x: x[1])")

    print("\nTask C: Filter positives")
    check(positives, expected=[3, 8, 4],
          hint="list(filter(lambda x: x > 0, numbers))")
