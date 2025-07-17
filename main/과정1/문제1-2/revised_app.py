from flask import Flask

app = Flask(__name__)

def hello():
    return "Hello, Devops!"

app.add_url_rule("/", view_func=hello)                       # sugar 문법 (syntactic sugar)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)



#app.add_url_rule("/", view_func=hello)  -----------> "주소-함수 연결을 수작업으로 등록해" 라는 직접 호출 문법
    # "앱에게 새로운 URL 규칙을 추가해줘. 누군가 '/' 주소로 요청을 보내면, hello() 함수를 실행하도록 해줘!"
    # url : 브라우저가 요청할 경로(예:/)
    # view_func : 이 URL에 대해 실행할 함수 이름
    # ----> 즉, "/" 주소에 들어오면 Flask는 hello() 함수를 뷰(view) 함수로 사용해요.

# sugar 문법 이란?
    # 기능은 똑같은데 더 짧고, 더 보기 좋고, 더 쓰기 쉽게 만든 문법 -> 즉, 원래 복잡한 코드를 감싸서 사람이 보기 좋고 쓰기 편하게 만든 문법

# 그렇다면, app.add_url_rule 은 sugar 문법인가? NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!
     # @app.route("/") 이게 sugar 문법임.   -> Flask가 편하게 쓰라고 데코레이터 형태로 감싼 것임.

# 그렇다면, 언더스코어 (_) 이건 왜 쓸까?
    # 함수 이름 안의 _ 는 "단어를 구분하기 위한 파이썬 스타일"
    # add_url_rule -> 세 단어를 붙인 함수 이름. 읽기 좋게 하려고  단어 사이를 _로 구분한 것일뿐


# _변수 -> "이건 내부용이야. 외부에서 직접 쓰지 마."
# __변수 -> 이름 맹글링(name mangling, 클래스 내부 보호)
    # 파이썬에서 클래스 내부에서만 쓰는 변수를 만들고 싶을때, 보통 _변수, __변수 처럼 씀.
    # 그런데, __변수는 단순한 "숨기기"가 아니라, 아예 이름을 살짝 바꿔버리는 기능을 함. 이걸 이름 맹글링 (name mangling)이라고 함.
    # 예시 : 
    # class Robot:
    #     def __init__(self):
    #         self.name = "Robo"
    #         self.__secret = "나는 비밀 코드야"
    # r = robot()
    # 
    # print(r.name)           # 출력 : Robo
    # print(r.__secret)       # X 오류 발생
    
        # class(클래스)는 프로그래밍에서 아주 중요한 개념.  어떤 덩어리(개념, 주제)를 표현하는 "묶음" -> "동작을 묶는 틀"
        # class는 무언가를 만들기 위한 설계도 
        # 예시:
        # class TV:
        #    def power(self):
        #        print("TV 전원 ON!")
        #    def volume_up(self):
        #        print("소리 크게!")
        # my_tv = TV()
        # my_tv.power()

        # __init__  -> init 은 initialize 초기화하다, 처음 설정하다의 뜻
        # 예시 :
        # class Dog:
        #    def __init__(self):
        #        print("강아지 생성!")
        # d = Dog()  <--- 이때 __init__이 자동으로 실행됨.      __init__은 객체가 만들어질 때 자동으로 실행되는 함수.
               # 예시 2 :
               # class Person:
               #      def __init__(self, name):
               #           self.name = name
               # p1 = Person("민수")
               # print(p1.name)     -> 출력: 민수
                                                   # self 는 파이썬 클래스 안에서 약속된 중요한 기능성 단어
                                                   # self -> 자기자신(그 객체 자신)을 가리키는 약속된 이름.
                                                   # 예시: 
                                                   # class Person:
                                                   #       def say_hello(self):
                                                   #            print("안녕하세요")   -> 이때 self 는 말하는 주체가 누구냐를 지정하는 것.
                                                   # p1 = person()
                                                   # p1.say_hello()



# __init__ -> 매직 메서드 (특수한 역할을 하는 예약 함수)
# add_url_rule -> 단순한 함수 이름.