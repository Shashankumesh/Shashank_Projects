# Program to count duplicate characters in a string and return as dictionary

def count_duplicate_characters(s):
    s = s.lower().replace(" ", "")  # convert to lowercase and remove spaces
    char_count = {}

    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Create a dictionary of only duplicates
    duplicates = {char: count for char, count in char_count.items() if count > 1}

    return duplicates


# Taking input from the user
text = input("Enter a string: rrrrrrrrrrrrrccccccccbbbbbbbbbb")
duplicates = count_duplicate_characters(text)

if duplicates:
    print("Duplicate characters with counts:", duplicates)
else:
    print("No duplicate characters found.")
