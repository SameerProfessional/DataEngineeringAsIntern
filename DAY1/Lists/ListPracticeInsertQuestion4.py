# Create an empty list and insert five names using insert() only (don’t use append()).

Names = [] # Initialized an empty Names list

count = 5 # As it is given in the question

name = '' # Initialized the empty name variable 

# Take input of all the names

for i in range(count): # Loop from 0 to count-1
    name = input(f"Enter the {i+1} name : ")
    Names.insert(i, name)

# Get all the names of the cities

print("Cities of the list are :", Names)