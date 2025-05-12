nested = [] # Initialized the empty list
# We will store all rows entered by the user 

rows = int(input("Enter the number of rows: ")) # Take the number of rows from the user

# Take the nested list as input 
for i in range(rows): # Loop from 0 to rows-1
    row = input(f"Enter row {i+1} values seperated by space: ").split() # input().split() takes user input and splits it into strings.
    # The .split() method is used to divide a string into multiple parts based on a seperator.
    # By default, it splits wherever there is space and returns a list of strings.
    row = [int(x) for x in row] # Used list comprehension to convert the each string to integer
    nested.append(row) # Store the row in the nested list.

# Get all the elements of the nested list

print("Elements of the nested list are :", nested)



    