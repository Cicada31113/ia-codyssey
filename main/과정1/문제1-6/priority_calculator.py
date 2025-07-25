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


def evaluate_flat_expression(tokens):
    try:
        # 숫자 자리 확인 및 변환
        for i in range(0, len(tokens), 2):    # 짝수 인덱스만 순회하게 만들어주는 코드
            tokens[i] = float(tokens[i])

        # 1️⃣ 곱셈/나눗셈 처리
        i = 1
        while i < len(tokens) - 1:
            if tokens[i] == '*':
                result = multiply(tokens[i-1], float(tokens[i+1]))
                tokens[i-1:i+2] = [result]
            elif tokens[i] == '/':
                result = divide(tokens[i-1], float(tokens[i+1]))
                tokens[i-1:i+2] = [result]
            else:
                i += 2

        # 2️⃣ 덧셈/뺄셈 처리
        result = tokens[0]
        for i in range(1, len(tokens), 2):
            op = tokens[i]
            num = float(tokens[i+1])
            if op == '+':
                result = add(result, num)
            elif op == '-':
                result = subtract(result, num)
            else:
                return "Invalid input."

        return result

    except ZeroDivisionError as zde:
        return str(zde)
    except:
        return "Invalid input."


def evaluate_with_parentheses(tokens):
    stack = []
    i = 0
    while i < len(tokens):
        if tokens[i] == '(':
            sub_expr = []
            depth = 1
            i += 1
            while i < len(tokens) and depth > 0:
                if tokens[i] == '(':
                    depth += 1
                elif tokens[i] == ')':
                    depth -= 1
                if depth > 0:
                    sub_expr.append(tokens[i])
                i += 1
            sub_result = evaluate_with_parentheses(sub_expr)
            if isinstance(sub_result, str):  # 에러 메시지 전파
                return sub_result
            stack.append(str(sub_result))
        else:
            stack.append(tokens[i])
            i += 1

    # 괄호 없는 단일 계산
    return evaluate_flat_expression(stack)


def main():
    expr = input("Enter expression (use space between all tokens):\n> ")
    tokens = expr.strip().split()
    result = evaluate_with_parentheses(tokens)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
