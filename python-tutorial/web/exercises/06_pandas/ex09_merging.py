"""
EXERCISE 9: Merging DataFrames (Joins)

R vs Python:
    R:      left_join(df1, df2, by="key")
            inner_join(df1, df2, by="key")
    Python: df1.merge(df2, on="key", how="left")
            df1.merge(df2, on="key", how="inner")

Join types (same as SQL/R):
    how="inner"  - Only matching keys (default)
    how="left"   - All from left, matching from right
    how="right"  - All from right, matching from left
    how="outer"  - All from both

Key arguments:
    on="key"           - Same column name in both
    left_on, right_on  - Different column names
    suffixes=("_x", "_y")  - For overlapping column names

Example:
    orders = pd.DataFrame({"order_id": [1, 2], "customer_id": [101, 102]})
    customers = pd.DataFrame({"customer_id": [101, 103], "name": ["Alice", "Carol"]})

    orders.merge(customers, on="customer_id", how="left")
    # Order 2 will have NaN name (customer 102 not in customers)

TASK:
Given orders and customers:
1. Inner join (only orders with matching customers)
2. Left join (all orders, customer info where available)
3. Join with different key names (using left_on, right_on)
"""
import pandas as pd

orders = pd.DataFrame({
    "order_id": [1, 2, 3, 4],
    "customer_id": [101, 102, 101, 103],
    "amount": [50, 75, 30, 100]
})

customers = pd.DataFrame({
    "customer_id": [101, 102, 104],
    "name": ["Alice", "Bob", "Dave"],
    "city": ["NYC", "LA", "Chicago"]
})

# Different key names example
orders_alt = pd.DataFrame({
    "order_id": [1, 2],
    "cust_id": [101, 102],  # Note: different column name
    "amount": [50, 75]
})

# ---- YOUR CODE HERE ----
# Task 1: Inner join orders and customers
inner_result = None

# Task 2: Left join orders and customers
left_result = None

# Task 3: Join orders_alt to customers
# orders_alt uses "cust_id", customers uses "customer_id"
different_keys_result = None
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task 1: Inner join")
    check(len(inner_result), expected=3,
          hint='orders.merge(customers, on="customer_id", how="inner")')
    check(set(inner_result["customer_id"]), expected={101, 102})

    print("\nTask 2: Left join")
    check(len(left_result), expected=4,
          hint='orders.merge(customers, on="customer_id", how="left")')
    # Order with customer_id 103 should have NaN name
    order_103 = left_result[left_result["customer_id"] == 103]
    check(order_103["name"].isna().iloc[0], expected=True)

    print("\nTask 3: Different key names")
    check(len(different_keys_result), expected=2,
          hint='orders_alt.merge(customers, left_on="cust_id", right_on="customer_id")')
