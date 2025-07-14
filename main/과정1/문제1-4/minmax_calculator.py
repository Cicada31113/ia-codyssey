# ✅ 최소값, 최대값을 직접 계산하는 프로그램 (min/max 내장 함수 사용 금지)

def main():
    # 1️⃣ 사용자로부터 숫자들을 입력받음 (공백으로 구분된 문자열)
    user_input = input("Enter numbers separated by spaces: ")
    
    # 2️⃣ 입력받은 문자열을 공백 기준으로 잘라 리스트로 만듦
    tokens = user_input.split()

    # 3️⃣ 각 문자열을 float으로 변환 (숫자가 아니면 예외 처리)
    try:
        numbers = [float(token) for token in tokens]
    except ValueError:
        print("Invalid input.")  # 숫자 외 입력이 있으면 오류 메시지 출력
        return

    # 4️⃣ 아무 숫자도 입력하지 않았을 경우 처리
    if not numbers:
        print("No numbers entered.")
        return

    # 5️⃣ 최소/최대 초기값을 첫 번째 숫자로 설정
    min_val = numbers[0]
    max_val = numbers[0]

    # 6️⃣ 나머지 숫자들을 반복하면서 min/max 직접 계산
    for num in numbers[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num

    # 7️⃣ 결과 출력
    print(f"Min: {min_val}, Max: {max_val}")

# 🔚 프로그램 시작점
if __name__ == "__main__":
    main()