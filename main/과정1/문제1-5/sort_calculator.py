def main():
    input_string = input("공백을 두고 숫자를 여러개 막무가내로 기입해주세요 ㄴ(^^)ㄱ : ")   #1
    input_list = input_string.split()                                             #1소멸 #2사용 
    
    try:
        numbers = [float(a) for a in input_list]                                  #2소멸 #3사용
     
    except ValueError:
        print("Invalid input.")
        exit() #프로그램 강제종료 명령어

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
    print("sorted:", *numbers)

if __name__ == "__main__":
    main()




#1 사용자입력 먼저 받고
#2 받은 입력을 내가 원하는 방향으로 쪼개고
#3 쪼개어 갖고 있는 입력값들을 리스트안에 가두고 정리후 저장 -> #3 갖고 이제 써먹기 시작

# 버블 정렬(Bubllt Sort) 이름의 유래 -> 거품이 위로 올라가는 모습처럼 작동하기 때문인데
# 거품이 든 콜라를 컵에 따르면, 큰 거품들이 서서히 위로 둥둥 올라오지? 버블정렬에서도 리스트의 가장 큰 숫자가 반복시 우측이동





# numbers= [23, 17, 89, 3], len(numbers)=4 라고 한다면, range(len(numbers) = range(4) = [0, 1, 2, 3]
# 그렇다면, i의 첫번째 시행이 [0] 이라고 한다면, i = 0, j in range(3)
# j = 0, numbers[0] 과 numbers [1] 비교 
# j = 1, numbers[1] 과 numbers [2] 비교
# j = 2, numbers[2] 와 numbers [3] 비교
# 그렇다면, i의 첫번째 시행이 [1] 이라고 한다면, i = 1, j in range(2)
# j = 0, numbers[0] 과 numbers [1] 비교
# j = 1, numbers[1] 과 numbers [2] 비교
# 그렇다면, i의 첫번째 시행이 [2] 이라고 한다면, i = 2, j in range(1)
# j = 0, numbers[0] 과 numbers [1] 비교
# 그렇다면, i의 첫번째 시행이 [3] 이라고 한다면, i = 3, j in range(0) -> 시행 종료
# 이걸 그대로 따라가본다면, 각각 i = 0 , i = 1, i = 2, i = 3 의 진행결과라고 할 때,
# i = 0 ) 
# j = 0 ) 23 > 17     ! 자리바꿈 발생 [17, 23, 89, 3]
# j = 1 ) 23 < 89    유지
# j = 2 ) 89 > 3      ! 자리바꿈 발생 [17, 23, 3, 89]
# i = 1 )
# j = 0 ) 17 < 23    유지
# j = 1 ) 23 > 3      ! 자리바꿈 발생 [ 17, 3, 23, 89]
# i = 2 )
# j = 0 ) 17 > 3      ! 자리바꿈 발생 [ 3, 17, 23, 89] 
 
# *numbers -> * 는 unpacking(풀기) 연산자임. 리스트 안의 값들을 하나씩 꺼내서 공백구분 출력함
# numbers = [10, 232, 2, 4]
# print(*numbers) -> 10 232 2 4

# 리스트 컴프리핸션 기억하기 [표현식 for 변수 in 반복가능한_것]