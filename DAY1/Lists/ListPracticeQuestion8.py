animals = [] # Initialized an empty list

# Take the input the number of elements of the list

number = int(input("Enter the number of elements in the list: "))

element = 0 # Initialized the element variable

# Take input the elements of the list

for i in range(number): # Loop from 0 to number-1

    element = input(f"Enter the {i+1} animal of the list : ")

    animals.append(element)

# Remove the third element of the list

del animals[2]

# Get all the elements of the list

print("Elements of ther list are:", animals)

# Remove a specific animal using .remove()

if "Dog" in animals:
    animals.remove("Dog")
else:
    print("Animal does not exist")

# Get all the elements of the list 

print("All the elements of the list are : {} ".format(animals))

# Remove the last animal using .pop()

removed_animal = animals.pop(-1)

# Get the removed element and all the elements of the list 

print("Removed element : {}, Elements of the list are : {}".format(removed_animal, animals), sep = '\n')