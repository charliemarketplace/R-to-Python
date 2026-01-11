"""
EXERCISE 7: Dictionary Comprehensions

R vs Python:
    R:      setNames(x^2, x)  # Named vector
    Python: {x: x**2 for x in range(1, 6)}  # Dict comprehension

Dictionary comprehensions create dicts from iterables.

Syntax: {key_expr: value_expr for item in iterable}
        {key_expr: value_expr for item in iterable if condition}

Examples:
    squares = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

    # From two lists:
    names = ['a', 'b', 'c']
    values = [1, 2, 3]
    d = {k: v for k, v in zip(names, values)}  # {'a': 1, 'b': 2, 'c': 3}

TASK A: Create a dict mapping numbers 1-5 to their cubes: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
TASK B: From the words list, create a dict mapping each word to its length.
        Only include words with length > 3.
"""

words = ['a', 'cat', 'elephant', 'dog', 'hi', 'python', 'r']

# ---- YOUR CODE HERE ----
cubes = None       # {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
word_lengths = None  # {'elephant': 8, 'python': 6} (only words with len > 3)
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: Number to cube mapping")
    check(cubes, expected={1: 1, 2: 8, 3: 27, 4: 64, 5: 125},
          hint="{x: x**3 for x in range(1, 6)}")

    print("\nTask B: Word lengths (only words > 3 chars)")
    check(word_lengths, expected={'elephant': 8, 'python': 6},
          hint="{word: len(word) for word in words if len(word) > 3}")
