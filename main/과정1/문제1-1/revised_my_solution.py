# 수정본


def greet(name = "world"):
    name = input("이름을 입력하세요: ")           # 보다 일반적인 인사 함수로 확장성 확보
                                              # 매개변수 name을 추가해서 "Hello" 외에
    if not name :
        name = "world"
    return f"Hello, {name}"                          # "Hello, Alice" 처럼 쓸 수 있게함.
                               # f-string 사용으로 문자열 포맷팅 직관적으로

def main():                    # print(hello())를 직접 호출하는 대신 main()함수 따로 정의
    print(greet())             # 이렇게 하면, 프로그램의 진입점(Entry Point)을 분리해서 관리가 쉬움

if __name__ == "__main__":
    main()




# def greet(name = "world"): 를 이해해보자
# "greet" 이라는 함수를 정의하고 있음. 이 함수는 name 이라는 매개변수(parameter)를 받게됨.
# 그리고 name = "world" 라고 되어있는 것은 
# 이 함수를 호출할 때 아무 값도 주지않으면, name은 기본적으로 "world"라는 값을 가지게 됨
# 이걸 기본값(default value)라고 부름