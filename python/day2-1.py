# class default
class AlticastIPTV:
    def __init__(self):
        # self는 java에서 this, 메모리에 올라가 있는 객체 자기 자신을 의미한다
        pass

class AlticastIPTV:
    def __init__(self):
        print("__init1__")

iptv = AlticastIPTV()

class AlticastIPTV:
    def __init__(self, a, b, c):
        print("__init2__")

iptv = AlticastIPTV(1, 2, 3) # 생성할 때 메서드랑 구분하기 어렵기 때문에 클래스는 대문자로 시작하는 것을 권장한다

class AlticastIPTV:
    passed_b = 4
    # self.passed_b가 생길 수는 있으나 이렇게 사용하는 건 '상수만'. 이런 방식의 사용은 권장하지 않음

    def __init__(self, a, b, c):
        self.passed_a = a # 객체 변수를 여기서 초기화
        print("__init3__")
        AlticastIPTV.passed_c = 10

iptv = AlticastIPTV(1, 2, 3)
print(AlticastIPTV.passed_b)
print(iptv.passed_a)
print(AlticastIPTV.passed_c)

