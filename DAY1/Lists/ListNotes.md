# List - Built-in Data Types in Python

A **list** in Python is a sequence of comma-separated items enclosed in square brackets `[]`. **Lists** are one of the **4** built-in data-types in python used to **store collection of data**, the other three are **Tuple**, **Set**, and **Dictionary**.

## Key Features of Python Lists

- **Ordered Collection**: Lists are ordered collections of items. Each item in a list has a unique position index, starting from `0`.
- **Heterogeneous Items**: Python lists may contain objects of different data types.
- **Mutable**: Lists are mutable, meaning their elements can be changed, added, or removed. However, this also makes them unhashable.
- **Duplicate Items**: A list may have the same item at more than one index position.

## Accessing and Modifying List Elements

- **Indexing**: To access values in a list, use square brackets `[]` with an index number. Indexing in Python starts at `0`, so:
    - The first element of the list is at index `0`.
    - The second element is at index `1`, and so on.
- **Slicing**: Slicing is used to **replace multiple items** in a list.
- **`.append()`** - It is used to **add a single element** to the end of the list.

## Common List Methods

- **`.remove()`**: This method removes the **first occurrence of the specified value** from the list. If the value is not found, it raises a `ValueError`. Note that `.remove()` does not return any value.

