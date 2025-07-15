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


def basic_mode():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
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
        print("Error: Please enter valid numbers.")
    
    input("Wanna return? Enter '0': ")


def expression_mode():
    def calculate_expression(expr):
        try:
            parts = expr.split()
            if len(parts) != 3:
                raise ValueError("입력 형식은 '숫자 연산자 숫자'여야 합니다.")
            num1, operator, num2 = parts
            num1 = float(num1)
            num2 = float(num2)

            if operator == '+':
                return add(num1, num2)
            elif operator == '-':
                return subtract(num1, num2)
            elif operator == '*':
                return multiply(num1, num2)
            elif operator == '/':
                if num2 == 0:
                    raise ZeroDivisionError("0으로 나눌 수 없습니다.")
                return divide(num1, num2)
            else:
                raise ValueError("허용되지 않는 연산자입니다. (+, -, *, / 만 가능)")

        except ValueError as ve:
            return f"입력 오류: {ve}"
        except ZeroDivisionError as zde:
            return f"수학 오류: {zde}"

    expr = input("Enter expression: ")
    result = calculate_expression(expr)
    print(f"Result: {result}")
    input("Wanna return? Enter '0': ")


if __name__ == "__main__":
    while True:
        choice = input("\nchoice : [1] basic / [2] expression / [q] quit: ")

        if choice == "1":
            basic_mode()
        elif choice == "2":
            expression_mode()
        elif choice == "q":
            print("계산기를 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 입력해주세요.")
