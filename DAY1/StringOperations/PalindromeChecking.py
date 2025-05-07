text = input("Enter the String: ")

if text:
    def check_Palindrome(text):
        text1 = text.lower()
    
        if text1 == text1[::-1]:
            return True
        else: 
            return False
    

if check_Palindrome(text):
    print("The string is a palindrome")
else:   
    print("The string is not a palindrome")
# The above code is a simple implementation of the palindrome checking algorithm. It checks if the string is equal to its reverse.

