# Conclusion

## 1. `int(input(...))`
- Reads **user input** as a string.

## 2. **`input()`**
- **Returns a string**

## 3. **`int()`**
- **Returns an integer**

## 4. **`range(number)`**
- **Returns a `range` object**, not a list or tuple.
- Creates a sequence from **`0 to number-1`**
- **Examples**:
    - **`print(r)`**: **Output: `range(0, 5)`**
    - **`print(type(r))`**: **Output: `<class 'range'>`**
    - **To see the values inside, convert it to a list or tuple**:
        - **`list(r)`**: **Output: `[0, 1, 2, 3, 4]`**
        - **`tuple(r)`**: **Output: `(0, 1, 2, 3, 4)`**

## 5. **`clear()`**
- **Return type of `clear()` method is `None`**
- Modifies the `mutable` data structure (like `list`, `set`, or `dictionary`) in place by removing all its elements.
- **Useful for `memory management`**

## 6. **`Indexing`**
- Allows access to a **single element** from a sequence using its position **`(index)`**.
- **Syntax**: **`sequence[index]`**
- Indexing returns one item.
- **Data type** of return item: **Same as individual element of the sequence**.
- Indexing starts at `0` and negative indexing starts from `-1`.

## 7. **`Slicing`**
- Extracts a subsequence using **`start`:`stop`:`step`**.
    - **start**: Index to start from (**`inclusive`**)
    - **stop**: Index to stop at (**`exclusive`**)
    - **step**: How many indices to jump (**`default is 1`**)
- **Return type**: Same type as original sequence.
    - **Sequence is a list**: **`returns a list`**
    - **Sequence is a string**: **`returns a string`**
    - **Sequence is a tuple**: **`returns a tuple`**

## 8. **`print()`**
- **Returns None**

## 9. **`append()`**
- The `append` method is used with lists to **add a single item at the end** of the list.
- **Return type**: **None**
- **`append()`** modifies the original list **in place**.
- **Use cases of `append()`**:
    - **Add items from user input**
    - **Build a list dynamically** (Adds computed values, results during execution)
    - **Append objects (e.g., dictionaries, tuples)**

## 10. **`insert()`**
- **Returns None**
- **Inserts item at the given index in a list.**
- **Shifts all the elements after it to the right.**
- **Negative index inserts counting from the end.**
- **Modifies the list in place.**
- **Use cases of `insert()`**:
    - **Insert at specific position**: Example: **`list.insert(2, 'item')`**
    - **Insert at beginning**: Example: **`list.insert(0, 'start_item')`**
    - **Insert based on user input**: Example: **`list.insert(user_index, value)`**
    - **Priority-based insertion**: Example: **`list.insert(0, 'high-priority')`** (**Queues or Custom data structure**)
    - **Insert Tuple, Dictionary at specific index**: Example: **`list.insert(1, {'key': 'value'})`**

### **`Note`**
- Use **`append()`** instead of **`insert(i, number)`** while building the initial list.
- **`insert(i, number)`** in a loop causes **`O(n²)`** behavior, while **`append()`** is **O(1)**.

## 11. **`enumerate()`**
- The **`enumerate()`** function adds a **counter** to an iterable and returns it as an **enumerate** object, which can be directly used in a for loop. It automatically adds a number (called an index) to each item.

### **Example**
```python
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
        print(index, color)
```

**Output**:
```
0 red
1 green
2 blue
```

### **Why use `enumerate()`?**
- Simplifies code by avoiding manual index tracking.
- Improves readability and reduces errors.
- Useful for iterating over items with their indices.
- Works with any iterable (e.g., lists, tuples, strings).
- Supports optional start index:
    ```python
    for index, color in enumerate(colors, start=1):
            print(index, color)
    ```
    **Output**:
    ```
    1 red
    2 green
    3 blue
    ```

### **Additional Notes**
- Returns an `enumerate` object, which is memory efficient.
- Can be converted to a list or tuple if needed:
    ```python
    list(enumerate(colors))  # [(0, 'red'), (1, 'green'), (2, 'blue')]
    ```

### **Real-life uses**
- **Changing an item in a list**: If you find a specific value, you can update it.
- **Reading a file line by line**: You can number each line when processing a file.
- **Starting index from a different number**: You can tell `enumerate` to start counting from a different number like 1 or 0.

**Syntax** :
**`enumerate(iterable, start=0)`**
    **iterable** :- a list, tuple, or any object that supports iteration.
    **start** :- (optional) the starting index (default is 0)