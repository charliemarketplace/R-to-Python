"""
EXERCISE 7: String Formatting with f-strings

R vs Python:
    R:      paste0("Hello, ", name, "!")
            sprintf("Value: %.2f", x)
    Python: f"Hello, {name}!"
            f"Value: {x:.2f}"

f-strings (formatted string literals) are Python's modern way to embed
expressions in strings. Prefix the string with 'f' and use {expression}.

Format specifiers (after the colon):
    {x:.2f}   - 2 decimal places
    {x:>10}   - right-align in 10 characters
    {x:,}     - add thousand separators
    {x:.1%}   - as percentage with 1 decimal

TASK A: Create a greeting string "Hello, Alice! You are 30 years old."
TASK B: Format the price as "$1,234.57" (with comma separator and 2 decimals)
TASK C: Format the ratio as a percentage "75.0%"
"""

name = "Alice"
age = 30
price = 1234.567
ratio = 0.75

# ---- YOUR CODE HERE ----
greeting = None     # "Hello, Alice! You are 30 years old."
price_str = None    # "$1,234.57"
percent_str = None  # "75.0%"
# ---- END YOUR CODE ----


# ---- GRADING (don't modify below) ----
if __name__ == "__main__":
    from grader.check import check

    print("Task A: Greeting")
    check(greeting, expected="Hello, Alice! You are 30 years old.",
          hint="Use f\"text {variable} more text\"")

    print("\nTask B: Price formatting")
    check(price_str, expected="$1,234.57",
          hint="Use f\"${price:,.2f}\" - comma for thousands, .2f for decimals")

    print("\nTask C: Percentage")
    check(percent_str, expected="75.0%",
          hint="Use f\"{ratio:.1%}\" - .1% formats as percentage with 1 decimal")
