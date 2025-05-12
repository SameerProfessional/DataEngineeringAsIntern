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
for index,element in enumerate(List1):
    frequency = 0
    for element1 in (List1):
        if List1[index] == element1 and frequency < len(List1):
            frequency+=1
    else:
        print("Element at index {} : {} and frequency of the element : {}".format(index, element, frequency))
        
    