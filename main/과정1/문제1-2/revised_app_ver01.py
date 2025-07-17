from flask import Flask

class MyApp(Flask):                                         # Flask 클래스를 상속해서 구조화하는 방식
    def __init__(self, import_name):                        # Flask를 클래스로 감싸서 객체지향 스타일로 구성
        super().__init__(import_name)                       # 앱 로직이 커질수록 이 구조가 관리하기 편함.
        self.add_url_rule("/", view_func=self.hello)

    def hello(self):
        return "Hello, Devops!"
    
app = MyApp(__name__)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)



    # class MyApp(Flask):  -> "MyApp"이라는 내 클래스를 만들거야, 그리고 그 클래스는 Flask를 상속받을거야!
    # 클래스 상속이란? 
        # 기존에 있는 클래스(Flask)의 기능을 그대로 물려받아 새 클래스(MyApp)를 만드는 것.
        # 비유 : 
        # Flask는 기본 기능이 다 들어 있는 웹앱 박스야.
        # 난 그 박스를 내 입맛대로 조금 바꿔서 쓰고 싶은거야!""

    # def __init__(self, import_name):      -> "MyApp을 만들 때 실행되는 초기 설정 함수야."
        # import_name -> Flask가 내부에서 경로 등 설정을 할 때 쓰는 이름
        # self -> 지금 이 클래스로 만든 객체 자신을 자동으로 넣어주는 자리.

    # super().__init__(import_name)
        # super() -> 부모 클래스(Flask)의 기능을 실행해줘! 라는 뜻.
        # -> Flask 클래스의 __init__을 먼저 실행해줘. 거기서 필요한 내부 설정을 다 해줄거야.
        # 비유 : 
        # 부모가 만든 기본 세팅(Flask 내부 세팅)을 먼저 실행해줘야.
        # 내가 그 위에 기능을 붙여도 오류가 안나!.

    # self.add_url_rule("/", view_func=self.hello)
        # self.hello는 현재 클래스(MyApp) 안에 있는 hello()함수를 뜻함.

    # app = MyApp(__name__)
        # "MyApp" 클래스(설계도)로 앱 객체를 하나 만든거야."
        # 이때 __init__ 이 자동실행되며 위에서 설정한 모든 내용이 적용됨.
        #  -> MyApp.__init__(app, __name__)   |||| self -> app 지금 만들어지고 있는 그 객체 자체 ||||| import_name ->name 외부에서 넘겨준값