# 파이썬은 배열이 없다
# 배열의 큰 특징
# 문자열이 있다면, 연속된 공간에 존재하는 것
# 대신 파이썬은 list 가 있음
# 자바의 Arraylist랑 비슷
# list는 사이즈가 정해져 있지 않음


l1 = []
l1.append("a")
l1.append("p")
l1.append("p")
l1.append("l")
l1.append("e")

print(l1)

l1.insert(0, "i")
l1.insert(0, "t")
l1.insert(0, "l")
l1.insert(0, "a")

print(l1)

l1.append("c")
l1.append("a")
l1[0] = 'hello'
print(l1)

print(l1.pop())  # 뒤부터 pop
print(l1.pop(0))  # 인자 빼옴

l2 = l1.copy()
l3 = l1[:]  # copy와 동일

l = ['a', 'b', 'c']
print(l)
print(l.index("a"))
# print(l.remove('a'))
print(l.count('b'))

l.reverse()
print(l)

l = [1, 5, 7, 8, 9, 3, 4, 2]
l.sort()
print(l)

l.sort(reverse=True)
print(l)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = l1 + l2
print(l3)

l1.extend(l2)
print(l1)

del l1[2]  # 3 이 지워짐
del l2[0:2]  # 5, 6 이 지워짐
print(l1)
print(l2)

l1[2:] = "del and append"
print(l1)

l1[2:] = ["dive"]
print(l1)

l1[1:2] = [5, 6, 7]
print(l1)