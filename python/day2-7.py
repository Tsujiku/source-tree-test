# 다이아몬드 관계
# 부모를 찾는 순서에 영향
# class Grand:
#     pass
#
# class Parent(Grand):
#     pass
#
# class Child(Grand, Parent):
#     pass
#
# c = Child()


# 아래는 가능
# class Grand:
#     pass
#
# class Parent(Grand):
#     pass
#
# class Child(Parent, Grand):
#     pass
#
# c = Child()
# print(Child.__mro__) # 메서드 찾는 순서 알려줌, metho resolution order


class Grand:
    def __init__(self):
        self.k = 10

c = Grand()

get_attrs = ('k', 'j')

print(c.k)
print(getattr(c, 'k'))
print(getattr(c, 'j', 'default'))
print(hasattr(c, 'j'))

c.pd_note = 40 # pd_note
# c.set_alias = 'pub_beer'
# print(c.set_alias)
# c.l1 = [1, 2, 3, 4]
# print(list(c.l1))
setattr(c, 'straghit', 'MBC')
print(c.straghit)

# 외부에서 정의한 변수는
# 정적 메서드 내에서 self나 cls로 넘겨서 사용 가능

class G:
    j = 14

    def __init__(self):
        self.k = 10

    def h(self):
        return getattr(self, 'k')

    @classmethod
    def ch(cls):
        return  getattr(cls, 'j')

c = G()
print(c.h())
print(G.ch())

