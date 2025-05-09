list1 = [] # Initialized the empty list

# Take input of the number of elements in the list
count = int(input("Enter the number of elements in the list: "))

element = 0 # Initialized the element variable 

# Take input of the elements of the list
for i in range(count): # Loop from 0 to count-1
    element = int(input(f"Enter the {i+1} element of the list: "))
    list1.append(element)

# Get all the elements of the List
print("Elements of the list are :", list1)

# Now we will use the clear method of the list

list1.clear()

# Get all the elements of the list
print("Elements of the list after using clear() method :", list1)