x = "adfdfdasaaa"


# BEST METHOD: Using dict.fromkeys() to preserve order (Python 3.7+)
# This is the most efficient and clean approach
def remove_duplicates(string):
    return ''.join(dict.fromkeys(string))


# Test the function
result = remove_duplicates(x)
#print(f"Original string: {x}")
print(f"Without duplicates: {result}")
