# for (int i = 0; i< max; i++ ) {...}

# entry 는 index
# in 뒤에는 반복할 수 있는 객체가 들어옴 - 문자열, list, tupple, set, dic, aggregation, byte문자열
for entry in "Hello AI":
    print(entry)

# dicionary
for entry in {'a': 'A', 'b': 'B'}:
    print(entry)

for entry in {'a': 'A', 'b': 'B'}.values():
    print(entry)

for entry in {'a': 'A', 'b': 'B'}.items():
    print(entry)

for entry in {'a': 'A', 'b': 'B'}.items():
    key = entry[0]
    value = entry[1]

for key, value in {'a': 'A', 'b': 'B'}.items():
    print(key)
    print(value)

# k = 1, 2, 3
# k1, k2, k3 = k


for key, value in {'a': 'A', 'b': 'B'}.items():
    if key == 'a':
        continue
else:
    print("거짓!")


a = 1
while a:
    if a > 10:
        break
    a += 1

a = [1, 2, 3, 4]
a2 = [1, 2, 3, 4]

while a:
    while a2:
        a2.clear()

while a:
    pass
else: # 조건이 거짓이 되면 실행함
    pass

