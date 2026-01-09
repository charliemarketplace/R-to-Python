"""
EXERCISE 1: Lists - Python's Workhorse

R vs Python:
    R:      c(1, 2, 3)      # Vector (homogeneous)
            list(1, "a")    # List (heterogeneous)
    Python: [1, 2, 3]       # List (can be heterogeneous)

Python lists are like R's lists - ordered, mutable, can hold mixed types.

Key list methods:
    lst.append(x)     # Add to end (modifies in place!)
    lst.extend([...]) # Add multiple items
    lst.insert(i, x)  # Insert at position i
    lst.pop()         # Remove and return last item
    lst.pop(i)        # Remove and return item at index i
    lst.remove(x)     # Remove first occurrence of x
    len(lst)          # Length
    x in lst          # Check membership

R uses c() to concatenate; Python uses + or .extend():
    R:      c(x, y)
    Python: x + y  or  x.extend(y)

TASK:
Perform the following operations on the list:
1. Append 6 to the end
2. Insert 0 at the beginning (index 0)
3. Remove the value 3 (not index 3!)
4. Pop the last element and store it in `popped`
"""

numbers = [1, 2, 3, 4, 5]

# ---- YOUR CODE HERE ----
# 1. Append 6 to the end

# 2. Insert 0 at the beginning

# 3. Remove the value 3

# 4. Pop the last element
popped = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Check final list:")
    check(numbers, expected=[0, 1, 2, 4, 5],
          hint="After all operations: [0, 1, 2, 4, 5]")

    print("\nCheck popped value:")
    check(popped, expected=6,
          hint="pop() returns and removes the last element")
