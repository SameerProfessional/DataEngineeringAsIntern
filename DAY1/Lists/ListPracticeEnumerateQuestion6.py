# Print only elements at odd positions.
# Input: [100, 200, 300, 400, 500]
# Output: 200, 400

List1 = [] # Initialize the empty list 

# Take input of the number of elements in the list

count = int(input("Enter the number of elements in the list : "))

element = 0 # Initialize the empty variable element

# Take the input of all the elements in the list

for i in range(count): # Loop from 0 to count-1
    element = int(input(f"Enter the {i+1} element of the list : "))

    List1.append(element)

# Get the elements at odd position
print("Elements at odd posistion are :", List1[1::2])

# Get the elements at odd position
for index, element in enumerate(List1):
    if index%2!=0:
        print(f"Element at index {index} :", List1[index])