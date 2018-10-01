class Alticast:
    pass

alti = Alticast()

# 객체에 런타임 시점에
alti.k = 1

def hello():
    return "hello Alticast"

alti.hello = hello
print(alti.hello())

