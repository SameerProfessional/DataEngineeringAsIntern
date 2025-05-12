# Write a python program that takes 5 colors from the user and stores them in a list.

Colors = [] # Initialized an empty list

# Take input of the number of colors from the user
count = int(input("Enter the number of colors : "))

element = 0 # Initialized an empty variable 

# Take input of the colors from the user
for i in range(count): # Loop from 0 to count-1
    element = input(f"Enter the {i+1} colour of the list : ")
    Colors.append(element) # Adding colors one by one to the end of the list

# Get all the colors of the list :
print("Colors of the list are :",Colors)

# Take input of the color from the user
color1 = input("Enter a new color that you want to add : ")

# Take input of the index at which you want to add

index1 = int(input("Enter the index at which you want to add : "))
if index1 <= len(Colors)-1 and index1>0: # length of the Colors list

# Add the color at the desired index
    Colors.insert(index1, color1)
else: print("Invalid Index")
# Take input of the color from the user
desired_color = input("Enter the color that you want to add : ")
# Insert a color at the 3rd index
Colors.insert(2, desired_color)

# Colors of the list are :
print("Colors of the list are :",Colors)









