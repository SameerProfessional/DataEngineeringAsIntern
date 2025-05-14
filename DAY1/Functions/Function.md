# Functions in Python

A function is a block of code that only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

## Defining a Function

In Python, a function is defined using the `def` keyword.

### Example:
```python
def my_function():
    print("Hello, world")
```

To call a function, use the function name followed by parentheses:

### Example:
```python
def my_function():
    print("Hello, world")

my_function()
```

---

## Arguments in Python

Arguments are the values passed to a function when it is called. They provide the function with the data it needs to perform its operations.

### Types of Arguments in Python

### 1. Positional Arguments
The order in which you pass the arguments must match the order of the parameters defined in the function.

#### Example:
```python
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}")

greet("John", "Doe")
```

#### Output:
```
Hello, John Doe
```

---

### 2. Keyword Arguments
Allows you to pass arguments by specifying the parameter name along with its value.

#### Example:
```python
def create_profile(name, age, occupation):
    return f"Name: {name}, Age: {age}, Occupation: {occupation}"

profile1 = create_profile(name="Alice", age=30, occupation="Engineer")
profile2 = create_profile(age=25, occupation="Engineer", name="Sameer")

print(profile1)
print(profile2)
```

#### Output:
```
Name: Alice, Age: 30, Occupation: Engineer
Name: Sameer, Age: 25, Occupation: Engineer
```

---

### 3. Default Arguments
Default arguments allow functions to be called with fewer parameters than initially defined.

#### Example:
```python
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Sameer", "Good morning")  # Output: Good morning, Sameer!
greet("Sameer")  # Output: Hello, Sameer!
```

---

### 4. Variable-Length Arguments
Allows a function to accept an arbitrary number of arguments.

#### Example:
```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(2, 3, 5))  # Output: 10
print(add_numbers(1, 2, 3, 4, 5, 6))  # Output: 21
```

#### Notes:
- `*args` collects all positional arguments into a tuple.
- Useful for utility functions like `sum`, `max`, etc.

---

### 5. Arbitrary Keyword Arguments
Allows a function to accept any number of named parameters.

#### Example:
```python
def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person(name="Sameer", age=25, country="India")
```

#### Output:
```
name: Sameer
age: 25
country: India
```

---

## Return Values

To let a function return a value, use the `return` statement.

#### Example:
```python
def my_function(x):
    return 5 * x

print(my_function(3))  # Output: 15
print(my_function(5))  # Output: 25
print(my_function(9))  # Output: 45
```

---

## The `pass` Statement

A function definition cannot be empty. Use the `pass` statement to avoid errors.

#### Example:
```python
def my_function():
    pass
```

---

## Positional-Only Arguments

To specify that a function can have only positional arguments, add `/` after the arguments.

#### Example:
```python
def my_function(x, /):
    print(x)

my_function(3)  # Output: 3
```

---

## Keyword-Only Arguments

To specify that a function can have only keyword arguments, add `*` before the arguments.

#### Example:
```python
def my_function(*, x):
    print(x)

my_function(x=3)  # Output: 3
```

---

## Combining Positional-Only and Keyword-Only Arguments

You can combine both argument types in the same function. Any argument before `/` is positional-only, and any argument after `*` is keyword-only.

---

## Best Practices: `if __name__ == "__main__"`

Adding a `main()` function along with the `if __name__ == "__main__"` guard ensures that code only runs when the script is executed directly, not when imported as a module.

#### Example:
```python
def main():
    print("The script is being run directly")

if __name__ == "__main__":
    main()
```

### Why Use This?
- Prevents automatic execution when the script is imported elsewhere.
- Keeps your code modular and organized.

---

## Pipelines in Data Science and Data Engineering

### What is a Pipeline?
A pipeline is a series of connected steps where the output of one becomes the input of the next.

#### Example:
```
Input -> Process1 -> Process2 -> Output
```

### Data Science Pipelines
Automates processes like:
1. Ingesting data
2. Cleaning data
3. Transforming features
4. Training a model
5. Evaluating the model
6. Deploying results (optional)

### Data Engineering Pipelines
Refers to ETL or ELT processes:
- **ETL**: Extract → Transform → Load
- **ELT**: Extract → Load → Transform (common with cloud data warehouses)

---

### Why Use Pipelines?
- **Automation**: Reduces manual intervention.
- **Reproducibility**: Ensures consistent results.
- **Modularity**: Simplifies debugging and maintenance.
- **Scalability**: Easily adaptable to larger datasets or cloud environments.
