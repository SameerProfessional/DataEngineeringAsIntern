# Replace all elements in a list that are greater than 10 with 0.

Numbers = [] # Initialized an empty Numbers List

# Take the input of the number of elements in the numbers
count = int(input("Enter the number of elements of the Numbers : "))

number = 0 # Initialized an empty variable number 

# Take the input of all the elements of the list

for i in range(count): # Loop from 0 to count-1
    number = int(input("Enter the number : "))
    Numbers.append(number)

# Get all the elements of the list are 
print("Elements of the list are :", Numbers)

# Replacement of the numbers in the list

for index, number in enumerate(Numbers): 
    if number > 10:
        Numbers[index] = 0

# Get all the elements of the list
print("Elements of the list are :", Numbers)