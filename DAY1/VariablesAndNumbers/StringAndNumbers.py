var = 5 
text = 'hello'
print(var * text)
# Output: hellohellohellohellohello (string repeated 5 times)
# # print(var + text)
# # Output: TypeError: unsupported operand type(s) for +: 'int' and 'str'

print(text, 5)

print(type(print(text, 5)))  # Output: <class 'NoneType'>