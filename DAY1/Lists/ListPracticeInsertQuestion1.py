# Create a list of 3 fruits. Insert a new fruit at the beginning of the list.

fruits = [] # Initialized the empty fruits list

# Input the number of fruits in the list

count = int(input("Enter the number of fruits : "))

fruit = 0 # Initialized the empty variable fruit

# Take input of all the fruits 

for i in range(count): # Loop goes from 0 to count-1
    fruit = input(f"Enter the {i+1} fruit of the list : ")
    fruits.append(fruit)

# Get all the fruits of the list
print("Fruits of the list are :", fruits)

# Input the fruit that has to be added in the beginning
fruit1 = input("Enter the fruit that has to be added : ")

# Adding the fruit in the beginning of the list
fruits.insert(0, fruit1)

# Get all the fruits in the list
print("Elements of the list are :", fruits)
