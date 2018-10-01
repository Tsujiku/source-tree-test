#Bool
a = True
b = False

i = 0
f = 0.0
j = 0j
s1 = ""
l = []
t = tuple()
d = {}
s2 = ()
None
False

# 아래는 모두 false
i = int()
f = float()
j = complex()
s1 = str()
l = list()
t = tuple()
d = dict()
s2 = set()
b = bool()

print(i)
print(f)
print(j)
print(s1)
print(l)
print(t)
print(d)
print(s2)
print(b)

# byte 데이터가 깨지지 않게
a = "한글".encode("UTF-8")
print(a)
a = "한글".encode("euc-kr")
print(a)
a = "한글".encode("cp949") # code page 949, by MS
print(a)
a = "한글".encode("ksc5601")
print(a)
a = "한글".encode("iso-2022-kr")
print(a)

print(a.decode('iso-2022-kr'))

