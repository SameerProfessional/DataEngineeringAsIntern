List1 = [] # Initialize an empty list for the first list

List2 = [] # Initialize an empty list for the second list

List3 = [] # Initialize an empty list for the third list

# Get the number of elements in the first list

n1 = int (input("Enter the number of elements in the first list: "))

element = 0 # Initialize the element variable

# Get the elements of the first list
for i in range(n1): # Loops from 0 to n1-1
    element = input(f"Enter the {i+1} element of the first list:") # It will take input as string
    List1.append(element)

print("The elements of the first list are:", List1)

# Get the number of elements in the second list

n2 = int(input("Enter the number of elements in the second list: "))

# Get the elements of the second list
for i in range(n2): # Loops from 0 to n2-1
    element = int(input(f"Enter the {i+1} element of the second list: ")) # It will take input as integer
    List2.append(element)

# Enter the elements of the third list

n3 = int(input("Enter the number of elements in the third list: "))

# Get the elements of the third list
for i in range(n3): # Loops from 0 to n3-1
    element = float(input("Enter the {} element of the third list: ")) # It will take input as float
    List3.append(element)

MergedList = List1 + List2 + List3 # Merge the three lists
print("The merged list is:", MergedList)

# Note - The __add__ method is used to concatenate two lists. It does not modify the original lists, but returns a new list that is the result of the concatenation. The original lists remain unchanged.
# You can only add two lists at a time. To add three lists, you can use the __add__ method twice, or you can use the + operator to concatenate the lists. The + operator is more concise and easier to read.
