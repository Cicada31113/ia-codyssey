def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by Zero."
    return a / b

if __name__ == "__main__":
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /): ")

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = subtract(a, b)
        elif operator == "*":
            result = multiply(a, b)
        elif operator == "/":
            result = divide(a, b)
        else:
            result = "Invalid operator."

        print(f"Result: {result}")
    
    except ValueError:
        print("Error: Please enter valid intergers.")