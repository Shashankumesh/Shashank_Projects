name = "shashank"


# BEST METHOD: Using dict.fromkeys() to preserve order (Python 3.7+)
# This is the most efficient and clean approach
def remove_duplicates(name):
    return ''.join(dict.fromkeys(name))


# Test the function
result = remove_duplicates(name)
#print(f"Original string: {name}")
print(f"Without duplicates: {result}")
