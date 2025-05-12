nested = [] # Initialize the empty List

# Take the number of rows as input

rows = int(input("Enter the number of rows as input : "))

row = 0 # Initialized the empty row variable
row1 = []

# Take input of the elements
for i in range(rows): # Loop from 0 to rows-1
    row = input(f"Enter row {i+1} values :").split() # Return comma seperated values
    for j  in row: # Loop from 0 to row-1
        try:
            j = int(j) # try converting it into integer
        except ValueError:
            try:
                j = float(j) # try converting it into float
            except ValueError:
                j = j
        row1.append(j)
    
    nested.append(row1)

    row1 = [] # row1 points to new list after each iteration 
    # If we use .clear() method it actually cleans the same list which is stored.

# Get the elements of the nested list

print("Elements of the nested list :", nested)
        

   