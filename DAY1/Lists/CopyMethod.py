List1 = [] # Initialized the empty list

# Take input the number of elements in the list
count = int(input("Enter the number of elements in the list: "))

element = 0 # Initialized the empty element

# Take input of the elements 
for i in range(count): # Loop from 0 to count-1
    element = list(input(f"Enter the {i+1} element in the list: "))
    List1.append(element)

# Now we will create a shallow copy of the list

shallow_copy = List1.copy() # Returns a shallow copy of the list

# Get all the elements of the list

print("Elements of the original list are :", List1)
print("Elements of the shallow list are :", shallow_copy)

# Even if the elements inside the original list are immutable (like integers, strings, or tuples), a shallow copy still copies the references to those elements - not the actual values. 
# However, since immutable objects cannot be changed, this shared reference does not cause side effects.

