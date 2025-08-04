# 📌 사칙연산 계산기 (괄호 우선 계산 포함) - 순서 정리 버전

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

# ✅ 괄호 포함 수식 처리 (재귀적으로 괄호 내부부터 계산)
def evaluate_with_parentheses(tokens):
    i = 0
    stack = []

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
            if isinstance(sub_result, str):
                return sub_result
            stack.append(str(sub_result))
        else:
            stack.append(tokens[i])
            i += 1

    return evaluate_flat_expression(stack)

# ✅ 괄호가 없는 평탄한 수식 계산
def evaluate_flat_expression(tokens):
    try:
        for i in range(0, len(tokens), 2):
            tokens[i] = float(tokens[i])

        # 곱셈/나눗셈 먼저 처리
        i = 1
        while i < len(tokens) - 1:
            if tokens[i] == '*':
                result = multiply(tokens[i - 1], float(tokens[i + 1]))
                tokens[i - 1:i + 2] = [result]
            elif tokens[i] == '/':
                result = divide(tokens[i - 1], float(tokens[i + 1]))
                tokens[i - 1:i + 2] = [result]
            else:
                i += 2

        # 덧셈/뺄셈 처리
        result = tokens[0]
        for i in range(1, len(tokens), 2):
            op = tokens[i]
            num = float(tokens[i + 1])
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

# ✅ 메인 실행부
def main():
    expr = input("Enter expression (use space between all tokens):\n> ")
    tokens = expr.strip().split()
    result = evaluate_with_parentheses(tokens)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
