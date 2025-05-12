# Take a list of integers and insert a new number just after the first even number.

Numbers = [] # Initialized the empty Numbers List

# Take the input of the numbers of integers

count = int(input("Enter the number of integers : "))

number = 0 # Initialized the empty number variable 

# Take the input of all the integers 

for i in range(count): # Loop from 0 to count-1
    number = int(input(f"Enter the {i+1} integer of the list : "))
    Numbers.insert(i, number)

# Get all the elements of the list

print("Integers of the list are :", Numbers)

# Insert a new number 

# Take the input of the new number
new_number = int(input("Enter the new integer : "))
freq = -1 # Initialized an freque variable with value -1
for x in Numbers:
    
    if x % 2 == 0: 
        freq += 1
        break
    else:
        freq += 1


Numbers.insert(freq+1, new_number)

# Get all the elements of the list 
print("Integers of the list are :", Numbers)
