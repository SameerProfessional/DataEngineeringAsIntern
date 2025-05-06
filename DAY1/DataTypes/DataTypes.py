# In python, you can explicitly specify the data type using construction functions.
# These functions convert values into specific types.
# For example, int() converts a value to an integer, float() converts a value to a float, and str() converts a value to a string.
x = str("Hello World")
print(type(x))  # Output: <class 'str'>

# Use-case 
# Storing and manipulating text data.
# Useful in logging, messaging systems and document processing.

x = int(20)
print(x) # Output: 20

# Use-case
# Counting, indexing, and performing airthmetic calculations.
# Useful in finance, statistics and data analysis.

x = float(20.5)
print(x) # Output: 20.5

# Use-case
# Storing decimal numbers and performing calculations with them.
# Measurement-based applications, currency handling and scientific computations.

x = complex(5-7j)
print(x) # Output: (5-7j)

# Use-case
# Storing complex numbers and performing calculations with them.
# Useful in electrical engineering, signal processing and quantum computing.

# A list is an ordered collection of items, which can be of different data types.
# A list keeps the order of items as they were added, and allows any type of data to be stored together.
# Lists are mutable, meaning you can change their content after creation.
# Lists are defined by having values between square brackets [ ].

x = list(("apple", "banana", "cherry"))
print(x) # Output: ['apple', 'banana', 'cherry']

# Use-case
# Storing multiple items in a single variable.
# Useful in data analysis, machine learning and web development.
# Lists are commonly used to store collections of items, such as user data, product lists, or any other group of related items.
# Lists are often used to store data that can change over time, such as user preferences or database queries.
# Lists are also used to store data that is generated dynamically, such as user input or data from an API.
# Lists are often used to store data that is processed in batches, such as data from a CSV file or a database query.
# Lists are often used to store data that is used in loops, such as iterating over a list of items or processing a list of user inputs.
# Lists are often used to store data that is used in functions, such as passing a list of items to a function or returning a list of items from a function.
# Lists are often used to store data that is used in classes, such as storing a list of objects or attributes in a class.
# Lists are often used to store data that is used in modules, such as importing a list of items from a module or exporting a list of items from a module.
# Lists are often used to store data that is used in packages, such as importing a list of items from a package or exporting a list of items from a package.
# Lists are often used to store data that is used in libraries, such as importing a list of items from a library or exporting a list of items from a library.
# Lists are often used to store data that is used in frameworks, such as importing a list of items from a framework or exporting a list of items from a framework.
# Lists are often used to store data that is used in applications, such as importing a list of items from an application or exporting a list of items from an application.
# Lists are often used to store data that is used in systems, such as importing a list of items from a system or exporting a list of items from a system.
# Lists are often used to store data that is used in networks, such as importing a list of items from a network or exporting a list of items from a network.



# A tuple is an ordered collection of items, which can be of different data types.
# Tuples are immutable, meaning you cannot change their content after creation.

x = tuple(("apple", "banana", "cherry"))
print(x) # Output: ('apple', 'banana', 'cherry')

# Use-case
# Storing multiple items in a single variable.
# Useful in data analysis, machine learning and web development.
# Tuples are commonly used to store constant data, such as configuration settings or fixed values.

# A range represents a sequence of numbers.

x = range(6)
print(x)

# Constructor does not return anything but creates an object.
# range is a built-in class in Python that represents an immutable sequence of numbers.
# When you write range(6), you are calling the constructor of the range class to create a range object that represents the numbers from 0 to 5 (inclusive).
# This object represents an immutable sequence of numbers, typically used for looping.
# The range object itself does not store the numbers in memory; it generates them on demand, which is memory efficient.

# When you write range(6), Python does not create a list of numbers right away. Instead, it creates a special object called a range object, which knows how to give you the numbers from 0 to 5 when you need them.

# This is good because:
    # It saves memory-it doesn't store all the numbers in memory.
    # It generates numbers on the fly, so you only get them when you need them.
    # It generates each number one at a time, only when needed(this is called "lazy evaluation").

# When you call range(6), you are actually this class to create a range object.

# x = range(6)

# Syntactic sugar :-
# x = range.__new__(range, 0, 6, 1)

# # The __new__ method is a special method in Python that is responsible for creating a new instance of a class. It is called before the __init__ method, which initializes the instance.
# # The __new__ method is typically used for immutable types, such as tuples and strings, where the instance cannot be modified after it is created.

# This uses the __new__ method of the range class to create an object with:
# Start = 0 (default if not provided)
# Stop = 6 
# Step = 1 (default if not provided)
# range(6) does not make the numbers right away
# It just stores the info needed to generate them later(start, stop, step).
# This makes it very memory efficient, especially for large ranges.

# Use-case:-
# Looping through numbers efficiently.
# Useful in data analysis, machine learning and web development.



# A dictionary is an unordered collection of unique items, which can be of different data types.
# Dictionaries are mutable, meaning you can change their content after creation.

x = dict(name = "Sameer", age = 25, city = "Varanasi")
print(x)

# dict is a built-in class in Python that represents a mutable mapping of key-value pairs.
# When you call dict(name = "Sameer", age = 25, city = "Varanasi"), you are calling the constructor of the dict class to create a dictionary object with the specified key-value pairs.

# Syntactic sugar :-
# x = dict.__new__(dict) 
# Now x is {}
# __init__ fills it 
# x.__init__(name = "Sameer", age = 25, city = "Varanasi")
# Now x is {'name': 'Sameer', 'age': 25, 'city': 'Varanasi'}
# key concept :
# __new__  = make the object (memory allocation)
# __init__ = initialize the object (data setup)


# __new__ is a special method that needs the class itself
# Signature of __new__ method:
# object.__new__(cls, *args, **kwargs)
# cls is the class itself, which is passed as the first argument to __new__.
# *args and **kwargs are the arguments that are passed to the constructor of the class.

# Why dict inside __new__?
# Because you are asking the base-level constructor system:
# "Make me a new empty object of class dict."
# That's why it is:
# dict.__new__(dict)
# If you wrote:
# dict.__new__(str)
# You would get a type error because str is not a subclass of dict. You are asking the dict constructor to create a str object, which does not make sense.
# Now let's say you try this instead :
# x = dict.__new__()
# Python will raise an error because __new__ needs the class itself as the first argument.
# TypeError: descriptor '__new__' of 'dict' object needs an argument.
# The __new__ method requires at least one argument, which is the 'class' of the object you want to create. In this case, you want a dict, so you must pass 'dict' as the first argument.
# __new__ is a class method that tells Python:
# "Make me a new object of this class."

# A set is an unordered collection of unique items. The items can be of different data types. Duplicate elements are automatically removed.
# Sets are mutable, meaning you can add or remove items after creation.
# Sets are defined by having values between curly braces { }.
# You can add only those elements to a set if they don't change after being added.
# What are immutable items ?
# These cannot be changed after creation, so they are safe to store in a set.
# Examples of immutable types :-
# int -> 1, 42, etc
# float -> 3.14, 2.678, etc
# str -> 'apple'
# tuple -> (1,2,3) (only if does contain a list inside) 

# What are mutable items ?
# These can be changed, and that makes them unsafe to store in a set - because a set relies on fixed hashes to manage uniqueness and lookup.
# Examples of immutable types :-
# list -> [1,2,3]
# set -> {1,2,3}
# dict -> {'a': 1}  
# What happens if you try this?
# s = set()
# s.add([1,2,3])
# you will get :
# TypeError: unhashable type: 'list'
# Because sets uses hashing to keep track of elements, and mutable types can't be reliably hashed.

x = set(("apple", "banana", "cherry")) # Creates a list
print(x)
print(type(x))

# Use-cases:
# Removing duplicates from a list.
# Membership Testing (Faster than Lists)
# Set Operations 
# Filtering unique words
# Set-Based logic in games or rule engines
# Comparing datasets
# Efficient data cleaning 
# Fast duplication in APIs or logs

# Frozenset is just like a set, except:
# It is immutable (cannot be changed after creation).
# It is hashable (can be used as a dictionary key or stored in another set).

# Frozensets are created using the frozenset() constructor.
# Frozensets are useful when you need a set that should not change, like keys in a dictionary or elements in another set.
# They are also useful when you want to ensure that the contents of a set remain constant throughout the program.

# How to create a frozenset?
# fs = frozenset([1,2,3,4,5,5,5,5])
# print(fs) # Output: frozenset({1, 2, 3, 4, 5})
# print(type(fs)) # Output: <class 'frozenset'>
# print(fs.add(6)) # Output: AttributeError: 'frozenset' object has no attribute 'add'
# print(fs.remove(1)) # Output: AttributeError: 'frozenset' object has no attribute 'remove'
# print(fs.discard(1)) # Output: AttributeError: 'frozenset' object has no attribute 'discard'
# print(fs.clear()) # Output: AttributeError: 'frozenset' object has no attribute 'clear'
# print(fs.pop()) # Output: AttributeError: 'frozenset' object has no attribute 'pop'
# print(fs.update([6,7,8])) # Output: AttributeError: 'frozenset' object has no attribute 'update'

# print(fs.intersection([1,2,3,4,5])) # Output: frozenset({1, 2, 3, 4, 5})

# Lists are allowed as input to frozenset() constructor.
# But lists cannot be elements inside a frozenset, because lists are mutable.
# list is converted into a frozenset.
# The frozenset removes duplicates and stores unique values.


