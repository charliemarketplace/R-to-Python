"""
EXERCISE 8: The Mutable Default Argument Trap - SOLUTION
"""


# ---- YOUR CODE HERE ----
def add_to_cart(item, cart=None):
    """Add an item to a shopping cart. Return the cart."""
    if cart is None:
        cart = []
    cart.append(item)
    return cart
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    cart1 = add_to_cart("apple")
    print("First call: add_to_cart('apple')")
    check(cart1, expected=["apple"],
          hint="First call should return ['apple']")

    cart2 = add_to_cart("banana")
    print("\nSecond call: add_to_cart('banana')")
    check(cart2, expected=["banana"],
          hint="Without fix, this returns ['apple', 'banana'] due to shared default!")

    my_cart = ["milk"]
    cart3 = add_to_cart("eggs", my_cart)
    print("\nThird call: add_to_cart('eggs', ['milk'])")
    check(cart3, expected=["milk", "eggs"],
          hint="When passing explicit cart, should add to that cart")
