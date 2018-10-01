# 믹스인 클래스, 자기 자신은 아무런 데이터를 안 가짐.
class Util:
    def hello(self):
        return getattr(self, 'k')

class Grand(Util):
    def __init__(self):
        self.k = 10

c = Grand()
print(c.hello())

class U:
    def __init__(self):
        self.k = 10

    def __add__(self, other):
        return self.k + other.k

class G:
    def __init__(self):
        self.k = 20

u = U()
g = G()

print(u + g)

class U:
    def __init__(self):
        self.k = 10

    def __radd__(self, other):
        return self.k + other.k

    def __mul__(self, other):
        return self.k * other.k

    def __sub__(self, other):
        return self.k - other.k

    def __floordiv__(self, other):
        pass

    def __truediv__(self, other):
        pass

class G:
    def __init__(self):
        self.k = 20

u = U()
g = G()

print(g + u)

