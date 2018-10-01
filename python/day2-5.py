# 상속
class Parent:

    def __init__(self):
        print("부모클래스의 초기화를 자식 생성자에서 자동으로 해주지 않음")

    def __del__(self):
        pass

    def traceback(self):
        print('p')

class Child(Parent):

    def __init__(self):
        super().__init__()
        self.__j = 10

    def __del__(self):
        pass

    def traceback(self, **k):
        print('c')

c = Child()
c.traceback()

# python은 접근 제한자가 없다 -> 모두 public이라고 생각하면 됨

# print(c.__j)
print(c._Child__j) # 사용 웬만하면 하지 마세요



