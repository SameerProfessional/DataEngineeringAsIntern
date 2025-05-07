text = input("Enter the String: ")

def first_And_Last_Character():
    global text;
# In python an empty string("") is considered as False.
    if text:
        print("First character in string: {} and last characeter in the string: {}".format(text[0], text[-1]))
    else:
        print("Empty String")
first_And_Last_Character()


