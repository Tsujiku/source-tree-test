# 비교 연산
class Util:
    def __new__(cls, *args, **kwargs):
        if 'instance' not in cls.__dict__:
            cls.instance = super(Util, cls).__new__(cls, *args, **kwargs)
        return cls.__dict__['instance']

    def __init__(self):
        print('__init__')

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

a = Util()