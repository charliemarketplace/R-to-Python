"""
EXERCISE 10: Shallow vs Deep Copy

THE TRAP:
    original = [[1, 2], [3, 4]]
    shallow = original.copy()  # or original[:]
    shallow[0][0] = 99
    print(original)  # [[99, 2], [3, 4]] - OOPS! Inner list shared!

Why? .copy() creates a NEW outer list, but the inner lists
are still the SAME objects (references copied, not data).

Solutions:
    import copy
    deep = copy.deepcopy(original)  # Recursively copies everything

R comparison:
    R uses copy-on-modify semantics - typically safer by default
    Python requires explicit deep copies for nested structures

When do you need deep copy?
- Nested lists/dicts that you want to modify independently
- Avoiding "action at a distance" bugs

When is shallow copy fine?
- Flat lists with immutable elements (numbers, strings)
- When you want changes to inner objects to be shared

TASK:
1. Create a shallow copy and demonstrate the problem
2. Create a deep copy that is truly independent
"""
import copy

original = {
    "name": "Alice",
    "scores": [85, 90, 95],
    "metadata": {"level": 1}
}

# ---- YOUR CODE HERE ----
# Task 1: Create shallow copy
shallow = None

# Task 2: Create deep copy
deep = None

# Now modify the copies (don't modify original!)
# These modifications should NOT affect original

# ---- END YOUR CODE ----

# Modify the copies after creation
if shallow is not None:
    shallow["scores"].append(100)  # This WILL affect original if shallow!
    shallow["name"] = "Modified"   # This WON'T affect original

if deep is not None:
    deep["scores"].append(200)     # This should NOT affect original
    deep["metadata"]["level"] = 99 # This should NOT affect original


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Check that original scores were affected by shallow copy:")
    # After shallow copy modification, original.scores has 100 appended
    check(100 in original["scores"], expected=True,
          hint="Shallow copy shares the inner list - original['scores'] should have 100")

    print("\nCheck that original name was NOT affected:")
    check(original["name"], expected="Alice",
          hint="Strings are immutable, so shallow copy name change is independent")

    print("\nCheck that original metadata was NOT affected by deep copy:")
    check(original["metadata"]["level"], expected=1,
          hint="Deep copy makes completely independent nested structures")

    print("\nCheck deep copy has modifications:")
    if deep is not None:
        check(200 in deep["scores"], expected=True)
        check(deep["metadata"]["level"], expected=99)
