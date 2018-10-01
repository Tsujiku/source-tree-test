# 집합
a = {1, 2, 3, 4}
print(a)

b = {3, 4, 5, 6}
print(a.intersection(b)) # 교집합
print(a.union(b)) # 합집합
print(a.difference(b)) # 차집합
print(b.difference(a))

# 위와 동일 연산
print(a & b)
print(a | b)
print(a - b)
print(b - a)

c = {3, 4}
print(c.issubset(a))
print(c.issubset(b))
print(c.issuperset(a))
print(a.pop())

