a = 0
b = 2

if a:
    pass # 참일 때, 아무것도 안함 꼭 4칸 띄어써야 함

if a and b:
    pass

if a or b:
    pass

c = 0
d = 0

if not a or b\
        and c:
    print("참")
elif d:
    pass
else:
    print("거짓")


if (b or c and a):
    print(True)
else:
    print(False)


a = ['a','b','c','d']
s = "a-b-c-d"
a1 = s.split("-")
print(a1)
print(a == a1)

print("-".join(a1) == s)

