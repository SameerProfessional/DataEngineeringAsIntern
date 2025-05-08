list1 = [] # Create an empty list

# Get the number of elements in the list
n = int(input("Enter the number of elements in the list: "))

# Get the elements of the list

element = 0 # Initialize the element variable
for i in range(n): # Loops from 0 to n-1
    element = int(input(f"Enter the {i+1} element of the list: "))
    list1.append(element)

print("The list is :", list1)


