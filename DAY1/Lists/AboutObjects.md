### **Objects Inside Objects: How It Works**  

In Python, **everything is an object**. This means that:  

1. **A list is an object** (of type `list`).  
2. **Every element inside the list—whether it’s a number, string, another list, or even a custom object—is also an object** with its own type.  
3. **The list holds references to these objects rather than storing the actual data itself**, meaning it doesn’t copy or embed objects, but simply points to them in memory.  

### **Example:**
```python
# Creating a list with different types of objects
my_list = [10, "hello", [1, 2, 3], {"key": "value"}]

# Checking the type of each element
for item in my_list:
    print(type(item))
```
### **Output:**
```python
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
```
Here, `my_list` contains four elements, and each one is an object of its respective type.

### **Nested Objects & References**  
Since lists store references to objects, they can **contain other lists, dictionaries, or even custom objects**. This allows for **deeply nested structures** where objects are inside objects.

#### **Example of Nested Lists:**
```python
nested_list = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(nested_list[0])    # Output: [1, 2]
print(nested_list[0][1]) # Output: 2
```
In this case:
- `nested_list[0]` is another list (`[1, 2]`), stored as a single element.
- `nested_list[0][1]` accesses the second element inside that sublist.

### **Understanding Object References**
Python uses **references** instead of duplicating objects inside a list. If you modify a mutable object inside a list, it affects the original object.

#### **Example:**
```python
original_list = [1, 2, 3]
my_list = [original_list]  # Storing a reference to original_list

original_list.append(4)  # Modifying the original list
print(my_list)  # Output: [[1, 2, 3, 4]]
```
Since `my_list` holds a **reference** to `original_list`, changes to the original list are reflected inside `my_list`.

### **Key Takeaways**
- Lists hold **references** to objects, not copies.
- Elements inside a list are also **objects**.
- Lists can **nest other objects**, including lists, dictionaries, and custom objects.
- Changes to **mutable** objects inside a list affect all references.
### **Objects Inside Objects: How It Works**  

In Python, **everything is an object**. This means that:  

1. **A list is an object** (of type `list`).  
2. **Every element inside the list—whether it’s a number, string, another list, or even a custom object—is also an object** with its own type.  
3. **The list holds references to these objects rather than storing the actual data itself**, meaning it doesn’t copy or embed objects, but simply points to them in memory.  

### **Example:**
```python
# Creating a list with different types of objects
my_list = [10, "hello", [1, 2, 3], {"key": "value"}]

# Checking the type of each element
for item in my_list:
    print(type(item))
```
### **Output:**
```python
<class 'int'>
<class 'str'>
<class 'list'>
<class 'dict'>
```
Here, `my_list` contains four elements, and each one is an object of its respective type.

### **Nested Objects & References**  
Since lists store references to objects, they can **contain other lists, dictionaries, or even custom objects**. This allows for **deeply nested structures** where objects are inside objects.

#### **Example of Nested Lists:**
```python
nested_list = [[1, 2], [3, 4], [5, 6]]

# Accessing elements
print(nested_list[0])    # Output: [1, 2]
print(nested_list[0][1]) # Output: 2
```
In this case:
- `nested_list[0]` is another list (`[1, 2]`), stored as a single element.
- `nested_list[0][1]` accesses the second element inside that sublist.

### **Understanding Object References**
Python uses **references** instead of duplicating objects inside a list. If you modify a mutable object inside a list, it affects the original object.

#### **Example:**
```python
original_list = [1, 2, 3]
my_list = [original_list]  # Storing a reference to original_list

original_list.append(4)  # Modifying the original list
print(my_list)  # Output: [[1, 2, 3, 4]]
```
Since `my_list` holds a **reference** to `original_list`, changes to the original list are reflected inside `my_list`.

### **Key Takeaways**
- Lists hold **references** to objects, not copies.
- Elements inside a list are also **objects**.
- Lists can **nest other objects**, including lists, dictionaries, and custom objects.
- Changes to **mutable** objects inside a list affect all references.


