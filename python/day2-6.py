# python은 다중 상속을 지원함
# 상속
class Parent:

    def __init__(self):
        print("부모클래스의 초기화를 자식 생성자에서 자동으로 해주지 않음")

    def __del__(self):
        pass

    def traceback(self):
        print('p1')


class Parent2:

    def traceback(self, **kwargs):
        print('p2')


class Child(Parent, Parent2):

    def __init__(self):
        # 아래의 방법으로 상속 받은 부모 초기화
        super(Child, self).__init__() # Child에 자신을 던져줌
        super().__init__()
        Parent.__init__(self)
        Parent2.__init__(self)
        self.__j = 10

    def __del__(self):
        pass

    def traceback(self, **k):
        super().traceback()
        Parent.traceback(self)
        Parent2.traceback(self)
        print('c')

c = Child()
c.traceback()

# python은 접근 제한자가 없다 -> 모두 public이라고 생각하면 됨

# print(c.__j)
print(c._Child__j) # 사용 웬만하면 하지 마세요

# Child에 traceback 이 없을 경우, 상속 받은 순서대로 찾아낸다
