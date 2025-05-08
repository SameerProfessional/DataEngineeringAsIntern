Colors = [] # Initialize an empty list for the first list

# Get the number of elements in the list
n = int(input("Enter the number of items in the list: "))

# Get the elements of theh list
element = 0 # Initialize the element variable

for i in range(n): # Loops from 0 to n-1
    element = input(f"Enter the {i+1} element of the list: ")
    Colors.append(element)

# Element at index 3
print("The element at index 3 is: ", Colors[3])

value1 = Colors[-2] # Get the second last element
print("The second last element is: ", value1)

# Elements in the list are :

print("The elements in the list are: ", Colors)

# Slice the colors to get ['green', 'blue']

start = int(input("Enter the start index: "))
end = int (input("Enter the end index: "))
print("The sliced list is:", Colors[start:end:1]) # The end index is not included

# Print the middle elemets using slicing
print("The middle elements are: ", Colors[1:-1:1])

# Print the middle three elements using slicing
Colors1 = Colors[1:-1:1]
print("The middle three elements are: ",Colors1[:3:1])

