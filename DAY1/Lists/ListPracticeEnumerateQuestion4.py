# Insert a value after each occurrence of a specific element.
# Input: [10, 20, 10, 30], insert 999 after each 10.
# Output: [10, 999, 20, 10, 999, 30]

List1 = [] # Initialized an empty List

# Take the input of the number of elements in the list

count = int(input("Enter the number of elements : "))

element = 0 # Initialized an empty variable element

# Take the input of all the elements in the list

for i in range(count): # Loop from 0 to count-1
    element = int(input(f"Enter the {i+1} element of the list : "))
    List1.append(element)

# Get all the elements of the list 
print("Elements of the list are :", List1)

# Insert a value after each occurence of a specific element

value = 999
target_value = 10

for index, element in enumerate(List1):
    if target_value == element:
        List1.insert(index+1, value)
    
# Get all the elements of the list 
for i in range(len(List1)): # Loop from 0 to len(List1)-1
    print(f"Element at index {i} :", List1[i])