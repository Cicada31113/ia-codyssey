def greet(name="world"):
    print("처음 name:", name)
    name = input("이름을 입력하세요: ")
    print("입력 이후 name:", name)

if __name__ == "__main__":
    greet()



# greet( ) 안에 값이 없으면 World 를 출력
# greet 함수 첫 프린트 ->  처음 name: ""
# input -> 이름을 입력하세요
# @@@@@@@@@@ 그렇다면 , input 이후의 print는 첫화면에서 출력되지 않는 이유는?
# 바로, input()이 실행되는 시점에 프로그램이 거기서 멈춰있기때문에, 그 아래 print() 줄이 실행이 안된 것처럼 보임
# @@@@@@@@@@ 그렇다면, 사용자입력후에는 왜 이전 print들은 안나올까?
# 바로, 안나오는게 아니라, 이미 나왔던거라 다시 안나오는거 