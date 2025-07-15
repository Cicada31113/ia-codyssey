def main():
    try:
        inputs = input("Enter numbers separated by space: ").split()
        numbers = [float(x) for x in inputs] #리스트 컴프리헨션 문법임

        min_val = numbers[0] #최소값 !!!!!!!! 
        max_val = numbers[0] #최대갑 !!!!!!!!아오

        for num in numbers[1:]:   # 리스트의 시작과 끝이라는 문법(슬라이싱 끝위치는 기입해놓으면 배제) 아오오오
            if num < min_val:
                min_val = num
            if num > max_val:
                max_val = num

        print(f"Min: {min_val}, Max: {max_val}")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
