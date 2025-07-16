def ahahaahahahaahha_sort():
    user_input = input("숫자를 공백으로 입력해라: ")
    
    if not user_input.strip():          #stirp()은 문자열 양쪽에 있는 공백 문자(스페이스,탭,줄바꿈 등)를 제거해줌
        print("Invalid input.")         # "  Hello  ".strip() -> "Hello"
        return                          #함수를 여기서 끝내겠다. 값은 반환하지않고, 그냥 함수 종료
                                        # if not user_input.strip():  
                                        # 의미 : 입력받은 문자열에서 공백을 다 지웠을때 아무것도 없다면 종료
                                        # return의 2가지 역할 1) return 값 (함수에서 값을 반환) / 2) 함수 즉시 종료

    try:
        nums = [float(x) for x in user_input.split()]
    except ValueError:
        print("Invalid input.")
        return
    
    while True:
        swapped = False                          # swapped 가 있었는지 확인해보자의 의미 (자리바꿈 여부 기록 시작)
                                                 # 이번 회차에 자리바꿈이 없었다고 가정하며 시작하는 것

        for i in range(len(nums) - 1):           # range(n) 0부터 시작하는 파이썬의 약속
            if nums[i] > nums[i + 1]:            # True, False는 파이썬 안에서 특별한 뜻을 가진 Boolean 값
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True                   # 자리 바꿈 발생시 기록

        if not swapped:                          # if not swapped는 if swapped == False: 랑 동일
            break                                # 자리 바꿈 없으면 반복 종료 
                                                 #(반대로 마지막 행위가 swapped = True)면 계속 while True 루프
    print("Sorted:", *nums)                      # for 반복문 한바퀴 돌때 쭉 False 떠야 not swapped에 해당

if __name__ == "__main__":
    ahahaahahahaahha_sort()


    #nums = [ 12, 182, 1, 17] // range(len(nums) - 1) = 3 // i = 0 , 1, 2
    #len(nums) = 4
    # i = 0) 
    # [0] [1] 비교 -> 12 < 182 False
    # i = 1)
    # [1] [2] 비교 -> 182 > 1  True 기록    [ 12 1 182 17 ]
    # i = 2)
    # [2] [3] 비교 -> 182 > 17 True 기록    [ 12 1 17 182 ]
    # <<<<< 마지막 행위 값이 True 였으므로 반복시행 >>>>> 현재 리스트 [ 12 1 17 182]

    # i = 0)
    # [0] [1] 비교 -> 12 > 1 True 기록    [1 12 17 182]
    # i = 1)
    # [1] [2] 비교 False
    # i = 2)
    # [2] [3] 비교 Fallse 
    # <<<<<< 하지만 반복문 안에 True 가 한 번이라도 있었으니 다시 반복시행>>>>> 현재 리스트 [ 1 12 17 182]

    # i = 0)
    # [0] [1] 비교 -> False
    # [1] [2] 비교 -> False
    # [2] [3] 비교 -> False
    # Not swapped 에 해당 ! -> break 


# if not <값>:
# -<값>이 False로 간주되는 값이면 -> not <값> -> True
# -<값>이 True로 간주되는 값이면 -> not <값> -> False
# 파이썬에서는 빈 문자열 ""도 False로 간주됨.
# user_input.strip() -> 사용자가 " " 같은 공백만 입력했을 경우 -> " "(빈문자열)
# not user_input.strip() -> not " " -> True -> 조건 만족 -> if 블록 내부 실행 !!!!
# 여기서 실행되는 블록은 pritn ("Invalid input.")
#                    return

# 파이썬은 모든 값에 대해 자동으로 True/False 판별 기준을 갖고 있음.
## if 문에서 어떤 값은 자동으로 False로 간주됨
### 예시 : " " 빈 문자열 // 0 숫자영 // [] 빈리스트 // None 값이없음 null같은 의미 // False (불린 값 자체)

# 불린(Boolean) 값이란? 오직두가지 값만 가지는 데이터 타입.
### 예시 : True <- 참 // False <-- 거짓
## 불린은 프로그래밍에서 조건을 판단할 때 꼭 필요함.
### 예시 : if hungry
###       eat()     여기서 hungry 는 True 일 때만 eat() 함수가 실행됨, hungry = False면 아무일도 안일어남
### 불린값이 표시되지않더라도, 파이썬은 내부에서 항상 True/False로 해석해서 조건문 판단함.







