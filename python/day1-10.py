#for (int i=0; i<10; i+= 2)

for item in range(0, 11, 2):
    print(item)

# 객체로 만듦 - 메모리 사용을 줄이기 위함

for item in sorted(range(0, 11, 2), reverse=True):
    print(item)

if 1 or 0 and 0:
    print(True)
else:
    print(False)