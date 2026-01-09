"""
EXERCISE 4: Multiple Return Values

R vs Python:
    R:      Returns a list: return(list(mean=m, sd=s))
            Access: result$mean, result$sd
    Python: Returns a tuple: return mean, std
            Access: mean, std = func()  (tuple unpacking!)

In Python, you can return multiple values by separating them with commas.
This creates a tuple, which can be unpacked into multiple variables.

    def get_stats(numbers):
        return min(numbers), max(numbers), sum(numbers)

    lo, hi, total = get_stats([1, 2, 3, 4, 5])
    # lo=1, hi=5, total=15

This is much cleaner than R's list()!

TASK:
Write a function `min_max_range(numbers)` that returns three values:
- The minimum value
- The maximum value
- The range (max - min)

Return them as a tuple (just use commas, no parentheses needed).
"""


# ---- YOUR CODE HERE ----
def min_max_range(numbers):
    """Return (min, max, range) of a list of numbers."""
    pass  # Replace with your implementation
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    test_numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

    print("Test 1: Check returned tuple")
    result = min_max_range(test_numbers)
    check(result, expected=(1, 9, 8),
          hint="Return minimum, maximum, max-min")

    print("\nTest 2: Unpack the values")
    minimum, maximum, range_val = min_max_range(test_numbers)
    check((minimum, maximum, range_val), expected=(1, 9, 8),
          hint="You can unpack: a, b, c = func()")

    print("\nTest 3: Another list")
    check(min_max_range([10, 20, 30]), expected=(10, 30, 20))
