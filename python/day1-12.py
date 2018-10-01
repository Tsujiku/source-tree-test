def hello():
    return None

print(hello())

# 필수 인자 3개 필요
def hello(a, b, c):
    return print(a, b, c)

hello(1, 2, 3)

# 인자에 기본값이 주어짐, 기본값인자는 맨 뒤에 들어와야 함
def hello(a, b, c=3):
    return print(a, b, c)

hello(1, 2, 3)

def hello(a, b=4, c=3):
    return print(a, b, c)

hello(1, 2, 3)

# 가변값 인자
def hello(a, b, c, d, *e):
    return print(a, b, c, d, e)

hello(1, 2, 3, 4, 5)
hello(1, 2, 3, 4, 5, 6)
hello(1, 2, 3, 4, 5, 6, 7)

# c:\free-board\res\
import os

def hello(*e):
    return os.sep.join(e)

print(hello("C:", "free-board", "res", "etc"))

def hello(*e):
    return "\\".join(e)

print(hello("C:", "free-board", "res", "etc"))

def h(a, b, c=1, d=2, e=3, f=4):
    return a, b, c, d, e, f

print(h(1, 2, f=10))

def h(a, b, c=1, d=2, e=3, f=4):
    return a, b, c, d, e, f

print(h(b=1, a=2, f=10)) # 순서를 바꿀 수 있다

def h(a, b, c=1, d=2, e=3, f=4, **keyword): # 가변 키워드 인자를 전달 할 수 있음. 명시되어 있지않은 인자를 넘겨받음
    return a, b, c, d, e, f, keyword

print(h(1, 2, f=10, g=20))

# 필수 기본 가변
def hello(a, b, c=1, *d):
    print(a, b, c, d)

hello(3, 4)
hello(3, 4, 5, 6, 7) # 순서대로 abcd에 들어감

def hellob(a, b):
    print(a, b)

a = (1,2)
hellob(*a)

def hellob(a, b):
    print(a, b)

a = {'a': 1, 'b': 2}
hellob(*a)
hellob(**a)

a = 13

def key_13():
    print(13)

def key_14():
    print(14)

def key_15():
    print(15)

key_action = {13: key_13, 14: key_14, 15: key_15}

b = key_action[a]() # list tupple 등에 함수를 담을 수 있음

# 파이썬의 함수는 무조건 하나를 반환함

t1 = (1, 2, 3, 4)
t2 = dict(j=4, k=10, b=50)

def ti_func(*args, **keywords):
    print(args, keywords)

t1_func(*t1)
t1_func(*t1, **t2)



