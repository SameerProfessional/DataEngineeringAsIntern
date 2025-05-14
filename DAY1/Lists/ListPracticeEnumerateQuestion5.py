# Remove elements from even indexes.
# Input: [5, 10, 15, 20, 25]
# Output: [10, 20] (indexes 1 and 3)

List1 = [] # Initialized an emmpty List

# Take the input of the number of elements in the list.
count = int(input("Enter the number elements in the list : "))

element = 0 # Initialized the empty element variable

# Take the input of all the elements in the list

for i in range(count): # Loop from 0 to count-1
    element = int(input(f"Enter the {i+1} element of the list : "))

    List1.append(element)

# Get all the elements of the lists
print("Elements of the lists :", List1)

# Remove element from the even indices
# del List1[::2]

# Get all the elements of the list

# print("Elements of the list are :", List1)

for index, element in enumerate(List1):
    if index % 2 == 0:
        del List1[index]

# Get all the elements of the list
print("Elements of the list are :", List1)
