a = 4
b = 5

# python의 함수는 무조건 결과값을 반환함, default is None
def sum1():
    pass

def sum2():
    return

print(sum1())
print(sum2())

# hash 값 출력 대상 - 문자, 숫자, tupple
a = "1"
b = "1"
print(a.__hash__())
print(b.__hash__())

# 1이 int인지 아닌지는 int 내부에 정의되어 있음
print(int("1"))

print(bin(1))
print(bin(10))
print(oct(10))
print(hex(10)) # 이 때의 값들은 문자열

print(int(oct(24), 8)) # 다시 숫자로

print("{:b}".format(10))
print("{:o}".format(10))
print("{:x}".format(10))

print(chr(65))
print(chr(54620)) # python 2 에서의 unichr과 같음

# print(dir("a"))

print(divmod(4, 3)) # tupple 형태

for i, entry in enumerate([1, 2, 3, 4], 1): # 1부터 시작
    print(i)
    print(entry)

help(print)

a="all"
print(isinstance(a, str))

a = [1, 2, 3, 4]
a_iter = iter(a)
print(next(a_iter)) # 하나씩 다음을 참조
print(next(a_iter))
print(next(a_iter))
print(next(a_iter))

print("1", "2", "3", "4", "5") # default 개행문자 들어감
print("1", "2", "3", "4", "5", end='') # 개행 없음
print("1", "2", "3", "4", "5", file=open("stdout.txt", "w"))
print("1", "2", "3", "4", "5", file=open("stdout.txt", "a"))

print(range(1, 11))
print(repr(range(1, 11)))

class A:
    pass

a = A()
print(a)

print(sum(range(1,100000)))

a = 1000000000000
print(type(a))

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9)

for item1, item2 in zip(a, b):
    print(item1, item2)
