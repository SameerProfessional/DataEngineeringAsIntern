# Write a function that takes a name as a parameter and prints "Hello, <name>!".

# Take the input of your name
name = input("Enter your name: ")

# Function that calls the greet_method()
def function_one(name='User'):

    print(f"Name is : {name}")
    
    greet_method(name)

# Function that is actually used to greet()
def greet_method(name='User'):

        print(f"Hello, {name}")

function_one()

function_one(name)

    