
strings = ["apple","apple","orange","kiwi","orange","banana","banana","guava","apple","guava"]

def remove_duplicates(strings):
    return list(set(strings))

# Example usage
#strings = ["apple","apple","orange","kiwi","orange","banana","banana","guava","apple","guava"]
print("Without duplicates:", remove_duplicates(strings))