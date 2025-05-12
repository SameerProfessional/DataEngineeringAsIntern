# Print all elements in a list with their indices.
# Example: Input: ['apple', 'banana', 'cherry'] → Output:
# 0 apple  
# 1 banana  
# 2 cherry

Fruits = [] #Initialize the empty list fruits

# Take the input of the number of fruits 
count = int(input("Enter the number of fruits in the list : "))

fruit = '' # Initialize the empty variable fruit

# Take input of all the fruits 
for i in range(count): # Loop from 0 to count-1
    fruit = input(f"Enter the {i+1} fruit in the list : ")
    Fruits.append(fruit)

# Get all the elements of the Fruits
print("Elements of the fruits :", Fruits)

# Get all the elements of the fruits with their indices

for index, fruit in enumerate(Fruits):
    print("Element at index {} is {}".format(index, fruit))

