# Insert a city name at the middle position of a list containing 5 cities.

Cities = [] # Initialized an empty list of cities 

count = 5 # As given in the problem

city = '' # Initialized an empty city variable

# Take input of all the cities 
for i in range(count): # Loop runs from 0 to count-1
    city = input(f"Enter the {i+1} city of the list: ")
    Cities.append(city)

# Get all the cities of the list
print("Cities in the list are :", Cities)

# Take input of the city 
city1 = input("Enter the city that you want to input : ")

Cities.insert(2, city1) # at the middle 

# Get all the cities of the list
print("Get all the cities of the list :", Cities)