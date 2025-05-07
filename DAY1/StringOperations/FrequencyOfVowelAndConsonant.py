text1 = input("Input a String")
text1 = text1.lower()
vowel = "aeiou"

def count_vowels_And_Consonants(text1, vowel):
    count = 0
    count1 = 0
    for char in text1:
        if char in vowel:
            count+=1
        else:
            count1+=1

    print("Frequency of vowel: {} and frequency of consonant: {}".format(count, count1))

count_vowels_And_Consonants(text1, vowel)

            
