# Count how many times a value appears along with its index.

List1 = [] # Initialized an empty list 

# Take the input of the number of elements of the List
count = int(input("Enter the number of elements : "))

element = 0 # Initialized an empty variable element 

# Take the input of all the elements 

for i in range(count): # Loop from 0 to count-1
    element = int(input("Enter the element : "))
    List1.append(element)

# Get all the elements of the list along with their frequencies
frequency = 0
Info = []
for element in (set(List1)):
    if element not in Info[::2]:
        Info = []
        for index1,element1 in enumerate(List1):
            if element == element1:
                Info.append(element1)
                Info.append(index1)
        print("Element is {},frequency is {} and the list of indices are {}".format(element, len(Info[1::2]), Info[1::2]))
    else:
        continue

    