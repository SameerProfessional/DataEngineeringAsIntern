# # Variables that are created outside of a function are called global variables.
# # Global variables can be accessed from any function in the program.

x = 'awesome'

def my_funct():
    print('Python is', x)
    print('Python is ' + x)
    print('Python is {}'.format(x)) # Output: Python is awesome
    # format() is a built-in function in Python that formats strings. It allows you to create a string with placeholders and then fill those placeholders with values.
    # You use curly braces {} as placeholders inside a string and then call the format() method on that string, passing in the values you want to insert into those placeholders.
    # The format() method replaces the placeholders with the values you provide in the order they are given.

    name = 'Sameer'
    age = 25
    hobby = 'coding'
    print('My name is {}, I am {} years old and I have a hobby of {}'.format(name,age, hobby)) # Output: My name is Sameer, I am 25 years old and I have a hobby of coding))
    print('My name is {0}, I am {2} years old and I have a hobby of {1}'.format(name, hobby, age)) # Output: My name is Sameer, I am 25 years old and I have a hobby of coding))
    
my_funct()

def hello_funct():
    firstName = 'Sameer'
    middleName = 'Singh'
    lastName = 'Gautam'
    birthPlace = 'Varanasi'
    global pi  
    pi = 3.14159265358979323846 # pi is a global variable.
    age = 25
    print("Hello, my name is {} {} {}. I was born in {}. I am {} years old.".format(firstName, middleName, lastName, birthPlace, age)) # Output: Hello, my name is Sameer Singh Gautam. I was born in Varanasi. I am 25 years old.))
    print("Hello, my name is {0} {3} {4}. I was born in {2}. I am {1} years old.".format(firstName, age, birthPlace, middleName, lastName)) # Output: Hello, my name is Sameer Singh Gautam. I was born in Varanasi. I am 25 years old.))
    print("Hello, my name is {firstName} {middleName} {lastName}. I was born in {birthPlace}. I am {age} years old.".format(firstName = firstName, middleName = middleName, lastName = lastName, birthPlace = birthPlace, age = age)) # Output: Hello, my name is Sameer Singh Gautam. I was born in Varanasi. I am 25 years old.))

# print('The value of pi is: {:.2f}'.format(pi)) # This will raise a NameError because pi is not defined yet.
# - The error occurs because the variable pi is defined inside the hello_funct() function, and it is not accessible outside of that function unless declared as global.
# - Accessing pi before defining it globally
# - You're trying to print pi before calling hello_funct(), but pi is only assigned inside hello_funct() after using the global keyword.
# - Before hello_funct() runs, pi doesn’t exist, leading to a NameError.


hello_funct()
print()
print('The value of pi is: {:.2f}'.format(pi))



# Note -> First call the function and then only you can access the value of global variable pi.
# - The global keyword allows you to modify the variable pi inside the function, making it accessible outside the function as well. 

# - The global keyword is only required inside a function when you want to modify a global variable from within that function. If you only want to read the value of a global variable, you don't need to use the global keyword.

value  = 10 # Global variable

def value_update_funct():
    value = 20 # Local variable
    print('Inside function:', value) # Output: Inside function: 20

value_update_funct()
print('Outside function:', value) # Output: Outside function: 10

# By default, if you assign a value to a variable inside a function, Python assumes it's a local variable(only available within that function). So, if you try to modify a global variable without using global keyword, Python treats it as a new local variable instead.

value1 = 75 # Global variable
def value_update_funct1():
    global value1 # Now we reference the global variable value1
    value1 = 97 # Modifying global variabe value1
    print('Inside function:', value1) # Output: Inside function: 97

value_update_funct1()
print('Outside function:', value1) # Output: Outside function: 97
# - The global keyword tells Python that you want to use the global variable value1 instead of creating a new local variable with the same name.

# You can modify global variables outside functions without global.
# Inside a function, global is neccessary if you want to change a global variable.
# Without global, pyrhon assumes you are creating a new local variabe, not modifying the global one.