# Program to reverse a number

def reverse_number(n):
    rev = 0
    while n > 0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev


# Taking input from the user
num = int(input("Enter a number: "))

if num < 0:
    print("Reversed number:", -reverse_number(-num))  # Handle negative numbers
else:
    print("Reversed number:", reverse_number(num))
