text1 = input("Enter a string: ")
text2 = input("Enter another string: ")
# found = False 
# bool is immutable in python, so we need to use a mutable type like list or dictionary to store the value of found.
# found = [False]
found = [False]  # Using a list to store the mutable value of found

def sub_String_exists(text1, text2):
    text1 = text1.lower()
    text2 = text2.lower()

    if len(text1) < len(text2):
        small_text = text1
        large_text = text2
    else:
        small_text = text2
        large_text = text1
    
# Now we will find the last index where the substring of small_text's length can start in large_text.
    last_index = len(large_text) - len(small_text) + 1
    for i in range(last_index):
        large_text_substring = large_text[i:i+len(small_text)]
        if small_text == large_text_substring:
           return True
        else:
            continue
    return False


if sub_String_exists(text1, text2):
    print("Substring exists")
else:   
    print("Substring does not exist")   
# The above code is a simple implementation of the sliding window technique to check if one string is a substring of another string.