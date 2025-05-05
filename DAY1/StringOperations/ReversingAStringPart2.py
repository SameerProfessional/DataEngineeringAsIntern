text = 'Sameer'

reversed_str = ''

for char in text:
    reversed_str = char + reversed_str  # Prepend each character to the reversed string
print(reversed_str)  # Output: reemaS
# text is a string, and in Python, a string is a sequence of individual characters.

# When you loop over it using for char in text, each char is just a 1-character string.

# So, char is not a data type, it's just a variable name — you could use any name: for x in text, for letter in text, etc.

