#  Given the list nums = [10, 20, 30, 40], change the value 20 to 25.

nums = [] # Initialized an empty list

# Initialize the element variable

element = 0 

# Get the number of elements to be added to the list

Number = int(input("Enter the number of elements to be added: "))

for i in range(Number):
    element = int(input(f"Enter the {i+1} element in the list: "))

    nums.append(element)


# Elements of the list are :

print("Elements of the list are: ", nums)

# Change the value 20 to 25

nums = [25 if x == 20 else x for x in nums]

# Get the elements of the list :

print("Elements of the list are : ", nums)

# Replace the value 30 and 40 with 35 and 45

nums = [35 if x == 30 else 45 if x == 40 else x for x in nums]

# Get the elements of the list :

print("Elements of the list are : ", nums)

# Append the number 50 to the list

nums.append(50)

# Get the elements of the list :
print("Elements of the list are : ", nums)
