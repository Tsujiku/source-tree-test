# 문자열이 식별자로 사용가능한지 알아보는 법
s = "abc"
print(s.isidentifier())

s = "try"
print(s.isidentifier())

import keyword

print(keyword.iskeyword(s))

help('del')

# 함수 다시, 필수 - 기본 - 가변 - 가변키워드
# 중첩 함수
def hello(a, g='hello', *args, **keywords):
    def pkg_install(a, g):
        print(a)

    def pkg_install2():
        print(a)

    pkg_install(2, 3)
    pkg_install2()

hello(1)

# 람다함수
# 재사용이 불가
(lambda: 1)

# map, filter, reduce
# map - 요소 하나 하나를 접근
# [1, 2, 3, 4, 5]
# * 2
# [2, 4, 6, 8, 10]

output = []
for entry in [1, 2, 3, 4, 5]:
    output.append(entry*2)
print(output)

output = map(lambda entry: entry * 2, [1, 2, 3, 4, 5])
print(list(output))

output = map(lambda entry: entry * 2, [1, 2, 3, 4, 5])
print(tuple(output)) # map의 결과는 iteratorㅋ

# filter - 근사값

# import math

from functools import reduce

result = reduce(lambda x, y : (x + y)*2, range(1, 11))
print(result)

# 람다함수도 가변 인자를 사용할 수 있다

def available_value():
    return 1, 2, 3, 4, 5

def check_value(val):
    if val > 3:
        return val

result = filter(check_value, [1, 3, 5, 2, 4, 8])
print(list(result))

##

print('partial***********')

from functools import partial

def available_value():
    return 1, 2, 3, 4, 5

def check_value(avail_list, val):
    if val not in avail_list:
        return None
    if val > 3:
        print(val)
        return val

check_value2 = partial(check_value, available_value())

result = filter(check_value2, [1, 3, 5, 2, 4, 8])
print(list(result))
println = print
print = partial(print, end="\n\n\n")
print("줄바꿈 없음")

