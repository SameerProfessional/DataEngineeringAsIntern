# Updating a single element using slicing
fruits = ['apple', 'banana', 'cherry']

fruits[1] = "blueberry" # Updated banana to blueberry

print(fruits)

# Updating Multiple elements using slicing

numbers = [1, 2, 3, 4, 5]

print("Numbers are : ", numbers)
numbers[1:4:1] = [20, 30, 40]
print("After updation numbers are : ", numbers)

# Updating elements at index 1 and 3

numbers[1:4:2] = [50, 70]
print("After updatng elements at index 1 and 3, numbers are: ", numbers)

# Adding elements to the list

List1 = [] # Initialized an empty list.

element = 0 # Initialized an element with 0.

# Get the number of elements in the list

num = int(input("Enter the number of elements in the list: "))

for i in range(num): # Loops from 0 to num-1
    element = int(input(f"Enter the {i+1} element of the list: "))
    List1.append(element)

# Elements of the list are:

print("Elements of the list are : ", List1)

# Adding element to the list 
num1 = int(input("Enter the element to be added: "))

List1.append(num1)

num2 = float(input("Enter the another element to be added to the list: "))

List1.append(num2)


var1 = input("Enter the text that to be added: ")

List1.append(var1)

# Elements of the list are :

print("Elements of the list are: ", List1)

# Adding another list 

List2 = []

# Get the number of elemens of the list
Number = int(input("Enter the number of elements of the lidst: "))

for i in range(Number): # Loops from 0 to Number-1
    element = float(input(f"Enter the {i+1} element of the second list : "))
    List2.append(element)

# Conacatating two lists

List3 = List1.__add__(List2)

print("Concatenation of the list1 and list2: ", List3)

 


