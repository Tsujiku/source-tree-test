l1 = []
for item in range(1, 6):
    l1.append(item * 2)

print(l1)

# list Comprehension
l2 = [item * 2 for item in range(1, 6)]
print(l2)

# list Comprehension
l2 = [item * 2 for item in range(1, 6) if item > 2] # 반복에 제한 조건을 줄 수 있음. dictionary도 가능
print(l2)

d1 = {'a': 'A', 'b': 'B'}

d2 = {}
for item in range(1,6):
    d2[item] = item
print(d2)

d3 = {item: item for item in range(1,6)}
print(d3)

d3 = {chr(item): item for item in range(65, 65 + 26)}
print(d3)

d3 = {chr(item): idx for idx, item in enumerate(range(65, 65 + 26))}
print(d3)

d3 = {chr(item): idx for idx, item in enumerate(range(65, 65 + 26), 1)}
print(d3)

t12 = (('a', '1'), ('b', '2'))
print(dict(t12))