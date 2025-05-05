

# Pattern1 Documentation

## Purpose
This file demonstrates a simple rectangular pattern of `*` symbols, where the number of rows and columns is fixed (5x5).

## Pattern Output
```
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```


## Code Explanation
1. **Symbol Definition:**
   - The `*` symbol is used to create the pattern.

2. **Outer Loop (Rows):**
   - The outer loop determines the number of rows in the pattern.
   - In this case, there are 5 rows.

3. **Inner Loop (Columns):**
   - The inner loop determines the number of symbols printed in each row.
   - Each row contains 5 symbols.

4. **Printing Behavior:**
   - The `end=' '` argument ensures that symbols are printed on the same line, separated by spaces.
   - A `print()` statement after the inner loop moves to the next line after completing a row.

## Key Points
- The pattern is a 5x5 grid of `*` symbols.
- Each row contains 5 symbols, separated by spaces.
- The script uses nested loops to generate the pattern.

## Usage
This pattern can be used as a basic example to understand nested loops and printing in Python.