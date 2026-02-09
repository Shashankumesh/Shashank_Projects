num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

if operation == "add":
    print("Result:", add(num_1, num_2))
elif operation == "subtract":
    print("Result:", subtract(num_1, num_2))
elif operation == "multiply":
    print("Result:", multiply(num_1, num_2))
elif operation == "divide":
    print("Result:", divide(num_1, num_2))
else:
    print("Invalid operation")