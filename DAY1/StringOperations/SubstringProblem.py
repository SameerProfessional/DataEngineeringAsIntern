# Problem: Check if one string is a substring of another string
# Solution: Use the 'in' operator to check if one string is a substring of another string. Sliding Window technique can be used to check for substrings.
# In Python, the 'in' operator is case-sensitive, so we need to convert both strings to lowercase before checking for a substring.


def sub_String_exists(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if len(text1) < len(text2):
        small_text = text1
        large_text = text2
    else:
        small_text = text2
        large_text = text1
    
    if small_text in large_text:
        print("Substring exists")
    else:
        print("Substring does not exist")

text1 = input("Enter a string: ")
text2 = input("Enter another string: ")
