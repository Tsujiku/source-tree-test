# python singleton
class Util:
    def __new__(cls, *args, **kwargs):
        if 'instance' not in cls.__dict__:
            cls.instance = super(Util, cls).__new__(cls, *args, **kwargs)
        return cls.__dict__['instance']

    def __init__(self):
        print('__init__')

    # def __dir__(self): # 외부에 보여줄 것을 제한함
    #     return []

    def __repr__(self):
        return '<Util value: k = 10>'

    # def __str__(self):
    #     return 'Obj'

a = Util()
b = Util()

print(id(a))
print(id(b))
print(a)
print(str(a))
print(hash(a))
print({a:'k'}) # dictionary에서 키값으로 문자열, 숫자 튜플이 가능했다. 여기에 키값으로 만든 class가 사용가능

