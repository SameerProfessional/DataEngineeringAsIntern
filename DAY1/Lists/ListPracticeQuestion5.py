fruits = [] # Initialized an empty list

# Get the number of elements in the list

number = int(input("Enter the number of the elements in the list: "))

element = 0 # Initialized the empty variable

# Get the elements in the list
for i in range(number): # Loops from 0 to number-1
    element = input(f"Enter the {i+1} fruit of the list: ")
    fruits.append(element)

# Remove the element at index 1

del fruits[1] # Use del when you know the index of the element you want to remove

# Get the elements of the list

print("Elements in the fruits list are: ", fruits)

# Delete a slice of elements:

del fruits[1:3] 

# Get the elements of the list

print("Elements in the fruits list are: ", fruits)

# .remove() method is used when you don't exactly which element(s) to delete

# Use .remove() when you know the value you want to delete(not the index)

Colors = []

# Get the number of elements in the list

num = int(input("Enter the number of elements in the list"))

# Take the inputs of elements :

for i in range(num): # Loops from 0 to num-1
    element = input(f"Enter the {i+1} color in the list: ")
    Colors.append(element)

# Remove the green element
if "Green" in Colors:
    Colors.remove("Green")
# Removes the first occurence of green
else:
    print('"Green" is not present in the list.')
# Get all the elements of the list
print("The elements of the list are: ", Colors)

# .remove() will raise an error if the value does not exist in the list

# Using pop() method
# If you want to remove and get that element, use .pop() 

numbers = [] # Initialized an empty list

# Take the input the number of elements in the list

frequency = int(input("Enter the number of elements in the list: "))

# Take the input of elements in the list.

for i in range(frequency):
    element = input(f"Enter the {i+1} number in the list: ")

    numbers.append(element)

# Remove and get element at index 1

removed_element1 = numbers.pop(1)

# Elements in the list are:

print("Removed element is {} andElements in the list are: {}".format(removed_element1, numbers))