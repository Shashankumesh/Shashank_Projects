# Reverse a number using string slicing
num = int(input("Enter a number:"))

# Convert to string, reverse, then back to int
reversed_num = int(str(num)[::-1])

print(f"The reverse of {num} is {reversed_num}")


# Reverse a string using slicing
text = input("Enter a string: ")
reversed_text = text[::-1]
print(f"The reverse of '{text}' is '{reversed_text}'")