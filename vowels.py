sentence = input("Enter a sentence: ")
def count_vowels(s):
    
    vowels = "aeiou"
    count = 0
    
    for char in s.lower():
        if char in vowels:
            count += 1
            
    return count
print("Number of vowels in the sentence:", count_vowels(sentence))
