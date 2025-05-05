text = 'Sameer'
# Never use str as a variable name, as it shadows the built-in str() function.
# str is a built-in function in Python that converts an object to a string.
rev_iterator = reversed(text) # Create a reverse iterator for the string 'Sameer'
# rev_iterator can be used only once. After that, it will be exhausted.
print(rev_iterator)  # Output: <reversed object at 0x...>
# When you use reversed(text), Python doesn't immediately create a reversed string. Instead, it creates a special object called an iterator, which stores the characters in reverse order, but doesn't display them until you ask for them. This is more memory-efficient, especially for large strings.
# To see the reversed string, you can convert the iterator to a list or join it into a string.

print(''.join(rev_iterator))  # Output: reemaS
# The join() method takes all items in an iterable (like a list or a string) and joins them into one string. The string that calls the join() method is used as a separator.

# In this case, the empty string '' is used as a separator, effectively concatenating the characters without any additional characters in between.

# The join() method is used to merge elements of an iterable(like a list or reversed(text) iterator) into a single string. The string that calls the join() method is used as a separator.
# In this case, the empty string '' is used as a separator, effectively concatenating the characters without any additional characters in between.
# The join() method is more efficient than using a loop to concatenate strings, especially for large strings or lists of strings.
# It avoids creating multiple intermediate strings, which can be memory-intensive.
# Instead, it creates a single string in one go, which is faster and uses less memory.
# This is particularly important in Python, where strings are immutable (cannot be changed in place). Each time you concatenate strings using the + operator, a new string is created, which can lead to performance issues for large strings or many concatenations.
# Its syntax is :-
# seperator.join(iterable)

print('-'.join(reversed(text)))  

words = ['Hello', 'Python', 'World']
print(' '.join(words))


