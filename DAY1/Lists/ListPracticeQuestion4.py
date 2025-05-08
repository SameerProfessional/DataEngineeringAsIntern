# Create a list of 4 cities. Then:

# Update the 2nd city name.

# Replace the last two cities with any new city names.

# Append another city at the end.

Cities = [] # Initialized the empty list 

# Get the number of elements in the list
number = int(input("Enter the number of cities in the list: "))
element = 0 # Initialized the element variable

# Get the elements of the List

for i in range(number): # Loops from 0 to number-1

    element = input(f"Enter the {i+1} element of the list")

    Cities.append(element)

# Update the second city name 

Cities[1] = input("Update the second city name : ")

# Replace the last two cities with any new city names

city1 = input("Enter the first new city name that needs to be replaced: ")

city2 = input("Enter the second new city name that needs to be replaced: ")

Cities[-2::1] = [city1, city2]

# Get the elements of the Cities list 

print("Elements of the Cities ")

# Append another city at the end

city3 = input("Enter the name of the city that you want to add")

Cities.append(city3)

# Get the elements of the Cities list :

print("Elements of the Cities are: ", Cities)