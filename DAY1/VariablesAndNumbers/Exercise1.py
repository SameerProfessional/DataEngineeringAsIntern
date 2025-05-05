x = 10
y = 3.5

print("x:", x, "y:", y)
print("x + y:", x + y)  # Addition
print("x - y:", x - y)  # Subtraction
print("x * y:", x * y)  # Multiplication
print("x / y:", x / y)  # Division
print("x // y:", x // y)  # Floor Division 
# The result is the largest integer less than or equal to the division result.
# For example, 10 // 3.5 = 2.0, which is the largest integer less than or equal to 2.857142857142857.
# It discards the decimal part (does not round to the nearest int, just drops everything after the decimal).
# Works for both integers and floats.

# print(7 // 2)     # 3  → because 7 ÷ 2 = 3.5 → floor = 3
# print(9 // 3)     # 3
# print(-7 // 2)    # -4 → because -3.5 floors to -4 (goes to the smaller int)

print("x % y:", x % y)  # Modulus (Remainder)
# The modulus operator (%) returns the remainder of the division of x by y.
# For example, 10 % 3.5 = 3.0, because 10 ÷ 3.5 = 2 with a remainder of 3.
# It works for both integers and floats.