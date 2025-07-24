def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero.")
    return a / b


def evaluate_expression(tokens):
    try:
        # 숫자와 연산자가 번갈아 있는지 확인
        if len(tokens) % 2 == 0:
            return "Invalid input."

        # 문자열 숫자를 float으로 변환
        for i in range(0, len(tokens), 2):
            tokens[i] = float(tokens[i])

        # 1️⃣ 곱셈, 나눗셈 먼저 계산
        i = 1
        while i < len(tokens) - 1:
            if tokens[i] == '*':
                result = multiply(tokens[i-1], float(tokens[i+1]))
                tokens[i-1:i+2] = [result]
            elif tokens[i] == '/':
                try:
                    result = divide(tokens[i-1], float(tokens[i+1]))
                    tokens[i-1:i+2] = [result]
                except ZeroDivisionError as e:
                    return str(e)
            else:
                i += 2  # 다음 연산자 위치로 이동

        # 2️⃣ 덧셈, 뺄셈 계산
        result = tokens[0]
        for i in range(1, len(tokens), 2):
            operator = tokens[i]
            number = float(tokens[i+1])
            if operator == '+':
                result = add(result, number)
            elif operator == '-':
                result = subtract(result, number)
            else:
                return "Invalid input."

        return result

    except:
        return "Invalid input."


def main():
    expr = input("Enter expression: ")
    tokens = expr.strip().split()
    result = evaluate_expression(tokens)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
