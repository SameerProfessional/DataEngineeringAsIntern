fruits = ['Apple', 'Lemon', 'Banana'] # Its a list of fruits.
# # A list is a collection of items that are ordered and changeable. It allows duplicate members.
# # The order in a python list refers to the sequence in which elements are added. Elements stay in the same order in which they are added.

# # Lists are defined by having values between square brackets [ ].

# # Lists are mutable, meaning you can change their content without changing their identity.

ab , bc , ca = fruits # Unpacking the list into variables.
print(ab, bc, ca , sep = '#######')

print(fruits) # The original list remains unchanged.
# # The original list is still intact and can be used as needed.
print(fruits[0], fruits[1], fruits[2], sep = '&&&&&')

# # If you want the list to be sorted alphabetically or numerically, you can use the sort() method.
# # # The sort() method sorts the list in ascending order by default. You can also specify the reverse parameter to sort in descending order.
# # # The sort() method modifies the original list in place and returns None. 

# # # The sort() method sorts the original list in place, meaning it does not create a new sorted list-it modifies the existing one. It return none because sort() does not return a new list.

new_list = fruits.sort() # This will sort the list in place and return None.
print(fruits, new_list, sep = ' ')
print('hello world')
fruits.append('Guava') # # # The append() method adds an item to the end of the list. It modifies the original list and does not return a new list.
new_fruits = fruits.__add__(['Papaya', 'Pineapple']) # The __add__() method adds two lists together and returns a new list. It does not modify the original list.
# # # The __add__() method is a special method in Python that allows you to use the + operator to concatenate two lists. It returns a new list that is the result of the concatenation.
fruits.append('Cherry')
# # # The sorted() function returns a new sorted list from the elements of any iterable (like a list, tuple, or string). It does not modify the original iterable.
print(type(new_list)) # This will return None.
new_list = sorted(fruits) # This will return a new sorted list.
print(fruits, new_list, sep = ' ')
print(type(new_list))
print(type(fruits))
print(new_fruits, new_fruits.sort(), sorted(new_fruits), sep = "  ") # Here print() is printing the return value of the sort() method, which is None.
print(new_fruits)

