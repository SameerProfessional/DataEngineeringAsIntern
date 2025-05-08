# Merging and sorting of two lists

List1 = [] # Initialize an empty list for the first list

List2 = [] # Initialize an empty list for the second list

List3 = [] # Initialize an empty list for the merged list


# Get the number of elements in the first list
n1 = int(input("Enter the number of elements in the first List: "))

# Get the elements of the first list
for i in range(n1): # Loops from 0 to n1-1
    element = int(input(f"Enter the {i+1} element of the first List: "))
    List1.append(element)

n2 = int(input("Enter the number of elements in the second List: "))

for i in range(n2): # Loops from 0 to n2-1
    element = int(input(f"Enter the {i+1} element of the second List: "))
    List2.append(element)

# Merge the two lists
List3 = List1.__add__(List2)

print("The merged List is :", List3)

# Sort the merged list in ascending order
List3.sort()
print("The sorted List is :", List3)
