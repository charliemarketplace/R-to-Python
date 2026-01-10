"""
EXERCISE 2: Tuples - Immutable Sequences

R doesn't have tuples. Python tuples are like immutable lists.

Tuple syntax:
    t = (1, 2, 3)       # With parentheses
    t = 1, 2, 3         # Parentheses optional (tuple packing)
    t = (1,)            # Single element needs trailing comma!
    t = ()              # Empty tuple

Tuples are:
- Immutable (can't change after creation)
- Hashable (can be dict keys, unlike lists)
- Often used for multiple return values
- Slightly more memory efficient than lists

When to use:
- Function return values
- Dict keys (need hashable type)
- Data that shouldn't change (coordinates, RGB colors)
- Unpacking: x, y, z = (1, 2, 3)

TASK A: Create a tuple `point` with coordinates (3, 4)
TASK B: Unpack `rgb` into variables red, green, blue
TASK C: Create a single-element tuple containing just 42
"""

rgb = (255, 128, 0)

# ---- YOUR CODE HERE ----
# Task A: Create tuple (3, 4)
point = None

# Task B: Unpack rgb into three variables
red = None
green = None
blue = None

# Task C: Single-element tuple (careful with syntax!)
single = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check, check_type

    print("Task A: point tuple")
    check(point, expected=(3, 4))

    print("\nTask B: Unpacked RGB values")
    check((red, green, blue), expected=(255, 128, 0))

    print("\nTask C: Single-element tuple")
    check(single, expected=(42,),
          hint="Single element tuple needs trailing comma: (42,)")
    check_type(single, tuple, hint="Must be a tuple, not an int")
