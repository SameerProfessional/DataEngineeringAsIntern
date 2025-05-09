# Python List `append()` Method

The `append()` method is used to add new objects to a list.

## Key Points:
- The method accepts an **object** as an argument and inserts it at the end of the existing list.
- In Python, everything is an object, and every object has a class (or type). When you use the `append()` method on a list, it takes a single object as an argument and adds it to the end of the list.
- Since everything in Python is an object, you can append any data type—whether it's a number, a string, another list, or even a custom object.

### Behavior with Lists:
- If you pass a list as an argument to the `append()` method, it will not treat the elements of the list as separate items to be added individually. Instead, it will add the entire list as a single element inside the original list.
- This means the original list will contain another list as one of its elements, and the size of the original list will only increase by one.

## Return Value:
- The method does not return any value but updates the existing list.