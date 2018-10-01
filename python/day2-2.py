# 가비지콜렉션

class AlticastIPTV:

    def __init__(self, a):
        self.passed_a = a
        pass

    # 클래스 내부에 함수는 '메서드'라고 부른다. 항상 self가 있어야 함
    def print(self, i, k=1, *args, **kwargs):
        print('alti')

    def __del__(self): # 어떠한 인자도 받지 않음
        print("__del__")

    # 정적 메서드
    def hello2():
        print('hello2')
    hello2 = staticmethod(hello2)

    # 데코레이터로 정적 메서드 만들기
    @staticmethod # hello3 = staticmethod(hello3)
    def hello3():
        # AlticastIPTV.passed_d = 10 이렇게 사용해야 됨 -> 클래스 메소드
        pass

    # 클래스 메소드
    def chello3(cls): # cls - 클래스 자기 자신, 여기서 AlticastIPTV
        alc = cls()
        alc.hello3()
    chello3 = classmethod(chello3)

    @classmethod
    def chello4(cls):
        pass

iptv = AlticastIPTV(10)
print(iptv.passed_a)
iptv.print(2)

AlticastIPTV.hello2()
AlticastIPTV.print(iptv, 11)