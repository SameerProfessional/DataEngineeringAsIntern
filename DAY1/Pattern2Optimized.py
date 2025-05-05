
def print_triangle(symbol="* ", rows=5):
    """
    Prints a right-angled triangle pattern using the specified symbol.
    The triangle has a height of 'rows' and each row contains an increasing number of symbols."""

    for i in range(1, rows + 1):
        print(symbol * i)
        # The multiplication of the string 'symbol' by 'i' creates a string with 'i' symbols.
        # This is a more efficient way to print the symbols in each row compared to using a nested loop.
        # The print function automatically adds a newline after each row, so no need for an additional print statement.
print_triangle("* ", 5)