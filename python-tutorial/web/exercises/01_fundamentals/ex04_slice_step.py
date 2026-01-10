"""
EXERCISE 4: Slice with Step

Python slice syntax: x[start:stop:step]
- step: how many indices to skip (default is 1)

Common patterns:
    x[::2]   - every 2nd element (even indices: 0, 2, 4, ...)
    x[1::2]  - every 2nd element starting from index 1 (odd indices)
    x[::-1]  - reverse the list!

R equivalent for reversing: rev(x)

TASK A: Extract every other element starting from the first: [1, 3, 5, 7, 9]
TASK B: Reverse the list to get [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ---- YOUR CODE HERE ----
result_a = None  # Every other element: [1, 3, 5, 7, 9]
result_b = None  # Reversed list: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check
    print("Task A: Every other element")
    check(result_a, expected=[1, 3, 5, 7, 9],
          hint="x[::2] means start at 0, go to end, step by 2")
    print("\nTask B: Reversed list")
    check(result_b, expected=[10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
          hint="A step of -1 goes backwards through the list")
