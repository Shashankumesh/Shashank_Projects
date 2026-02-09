# Python program to count vowels in a string

word = "shashank"
vowels = "aeiou"

# Count vowels
count = sum(1 for char in word if char in vowels)

# Find unique vowels
unique_vowels = set(char for char in word if char in vowels)

#print("Word:", word)
print("Total vowels:", count)
#print("Unique vowels:", unique_vowels)
print("Unique vowel count:", len(unique_vowels))

