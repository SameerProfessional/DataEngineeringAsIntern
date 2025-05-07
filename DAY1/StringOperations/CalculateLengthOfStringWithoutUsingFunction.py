text = input("Enter the String: ")

def calculate_length_Of_String():
    global text
    count = 0

    for char in text:
        count += 1
    return count

print("Length of the String:", calculate_length_Of_String())


