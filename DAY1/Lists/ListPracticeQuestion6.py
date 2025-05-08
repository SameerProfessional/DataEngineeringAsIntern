names = [] # Initialize the empty list.

# Take input the number of elements in the list.

number = int(input("Enter the number of elements in the list: "))

element = 0 # Initialized the element variable.

# Take input of the elements :
for i in range(number): # Loops from 0 to number-1
    element = input("Enter the {} name of the list: ")
    names.append(element)

# Remove the element at first index

del names[1]

# Get the elements of the list

print("Elements of the list are:", names)

# Remove the element "Orange" from the list

removed_element = names.remove("Orange")

# Get the removed element and all the elements of the list

print("Removed element : {} , Elements of the list are: {}".format(removed_element, names), sep = '\n')


