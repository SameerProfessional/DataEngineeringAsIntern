# Ask the user to enter 4 colors and store them in a list. Insert a color at the end using insert().

Colors = [] # Initialized the empty Colors list

count = 4 # As given in the problem

# Take input of all the colors from the user
for i in range(count): # Loop from 0 to count-1
    color = input("Enter the color : ")
    Colors.append(color)

# Get the list of all the colors

print("Colors of the list are :", Colors)


# Input the color from the user
color = input("Enter the color that you want to insert at the end :")
# Inserting the color at the end 
Colors.insert(len(Colors), color)

# Get all the colors of the list 

print("Colors of the list are :", Colors)



