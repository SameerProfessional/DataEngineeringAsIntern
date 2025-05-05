# Define the symbol to be printed
symbol = '*'

# Outer loop: Controls the number of rows in the pattern
for i in range(5):  # Loop runs from 0 to 4 (5 iterations)
    # Inner loop: Controls the number of symbols in each row
    for j in range(i):  # Inner loop runs 'i' times for each value of 'i'
        print(symbol, end=' ')  # Print the symbol without a newline, separated by a space
    print()  # Print a newline after each row to move to the next row

# Explanation of the loops:
# - When i = 0: range(0) ⇒ Inner loop doesn't run, only a newline is printed.
# - When i = 1: range(1) ⇒ Inner loop runs once, printing one symbol (*).
# - When i = 2: range(2) ⇒ Inner loop runs twice, printing two symbols (* *).
# - When i = 3: range(3) ⇒ Inner loop runs three times, printing three symbols (* * *).
# - When i = 4: range(4) ⇒ Inner loop runs four times, printing four symbols (* * * *).

# Key points:
# - The outer loop determines the number of rows in the pattern.
# - The inner loop determines the number of symbols printed in each row.
# - The `end=' '` argument ensures symbols are printed on the same line, separated by a space.
# - The `print()` after the inner loop moves to the next line after completing a row.