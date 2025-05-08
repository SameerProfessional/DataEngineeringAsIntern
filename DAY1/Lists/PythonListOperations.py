List1 = [] # Initialize the empty list
List2 = [] # Initialized the second empty list
List3 = [] # Initialized the third empty list

# Take input of the number of elements in the list

number = int(input("Enter the number of elements of the list :"))


element = 0 # Initialized the element variable

# Take input of all the elements of the list

for i in range(number): # Loop from 0 to number-1 

    element = int(input(f"Enter the {i+1} element of the list: "))

    List1.append(element)

# Get all the elements of the list 

print("Elements of the list are : ", List1)

# Take the input of the number of elements in the second list 

num = int(input("Enter the number of elements in the second list: "))

# Take input of the elements in the second list : 

for i in range(num): #$ Loop from 0 to num-1
    element = int(input(f"Enter the {i+1} element of the second list: "))

    List2.append(element)

# Concatenating the List1 and List2

List3 = List1.__add__(List2)

# Get all the elements of the list

print("Elements of the list are :", List3)


# Repetion with * operator 
# You can repeat a list multiple times using *.

Greet = ["Hello"]

print("Repeating the list :",Greet*5)

# Membership Operators "in" and "not in"
# These check if a value exists in the list
# Returns boolean value

Fruits = [] # Initialize the empty list

# Take input the number of elements in the list

frequency = int(input("Enter the number of elements in the list: "))

# Take input of the elements in the list

for i in range(frequency): # Loop from 0 to frequency-1
    element = input(f"Enter the {i+1} fruit in the list: ")
    Fruits.append(element)

# Checking the membership

is_exists = "Apple" in Fruits

is_exists1 = "Lemon" not in Fruits

# Get the membership details

print("Does Apple exist in Fruits? ", is_exists)
print("Lemon does not exist in Fruits? ", is_exists)


# Indexing and Slicing 
# Like Strings, you can index and slice list

index_slicing_List = [] # Initialized the empty list

# Take the input of the number of elements in the list 

count_elements = int(input("Enter the number of elements in the list: "))

# Take the input of the elements in the list

for i in range(count_elements): # Loop from 0 to count_elements-1

    element = input(f"Enter the {i+1} element of the list: ")

    index_slicing_List.append(element)

# Get the elements of the list

print("Elements of the list are : ", index_slicing_List)

# Get the third item in the list

third_item = index_slicing_List[2]

print("Third item in the list :", third_item)

# Get the second item from the end

second_last_item = index_slicing_List[-2]

print("Second item from the end:", second_last_item)

# Slice from index 1 to end

items_after_slicing = index_slicing_List[1::1]

print("Elements from index 1 to end are:", items_after_slicing)