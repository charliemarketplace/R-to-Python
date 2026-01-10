"""
EXERCISE 8: The Mutable Default Argument Trap

This is a FAMOUS Python gotcha that doesn't exist in R!

In Python, default argument values are evaluated ONCE when the function
is defined, not each time it's called. This means mutable defaults
(like lists or dicts) are SHARED across all calls!

WRONG:
    def add_item(item, lst=[]):  # BAD! Same list reused!
        lst.append(item)
        return lst

RIGHT:
    def add_item(item, lst=None):  # GOOD! Use None sentinel
        if lst is None:
            lst = []
        lst.append(item)
        return lst

TASK:
Fix the function `add_to_cart` below. Currently it has a bug where
items from previous calls persist. Use the None sentinel pattern.
"""


# ---- YOUR CODE HERE ----
# Fix this function using the None sentinel pattern
def add_to_cart(item, cart=[]):
    """Add an item to a shopping cart. Return the cart."""
    cart.append(item)
    return cart
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    # Test 1: First call with no cart should return single item
    cart1 = add_to_cart("apple")
    print("First call: add_to_cart('apple')")
    check(cart1, expected=["apple"],
          hint="First call should return ['apple']")

    # Test 2: Second call with no cart should ALSO return single item (new cart!)
    cart2 = add_to_cart("banana")
    print("\nSecond call: add_to_cart('banana')")
    check(cart2, expected=["banana"],
          hint="Without fix, this returns ['apple', 'banana'] due to shared default!")

    # Test 3: Explicit cart should work correctly
    my_cart = ["milk"]
    cart3 = add_to_cart("eggs", my_cart)
    print("\nThird call: add_to_cart('eggs', ['milk'])")
    check(cart3, expected=["milk", "eggs"],
          hint="When passing explicit cart, should add to that cart")
