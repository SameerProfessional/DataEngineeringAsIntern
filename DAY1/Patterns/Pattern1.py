symbol = '*'

for i in range(5): # This loop iterates 4 times for the rows
    # The outer loop controls the number of rows in the pattern.
    for j in range(5):# This loop iterates 4 times for the columns
        # The inner loop controls the number of symbols in each row.
        print(symbol, end=' ')
    print()  # This prints a new line after each row
#In Python, by default, print() adds a new line (\n) at the end of each printed item.
#The end=' ' argument changes this behavior by specifying what should be printed at the end instead of a new line.
