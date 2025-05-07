# Remove Duplicates in a List

List1 = []

# Get the number of elements in the list

n = int(input("Enter the number of elements: "))

for i in range(n): # Loops from 0 to n-1
    element = int(input(f"Enter the {i+1} element: "))
    List1.append(element)

print(List1)

List2 = list(set(List1))

print(List2)
