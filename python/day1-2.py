# tupple
# 모든 타입 다 담을 수 있지만
# 수정이 불가능 하다

t1 = (1, 2, 3, 4)
t2 = 1, 2, 3, 4
t3 = (1, )  # 한 개짜리 튜플을 만드려면 반드시 , 작성해야 함
t4 = 1,

print(t1)
print(t2)
print(t3)
print(t4)

# 튜플도 count, index 함수만 가짐

# 사전, 자바의 맵
# key - value
d1 = {'abc': 'alphabet'}
print(d1['abc'])  # 있으면 value 반환, 없으면 error
print(d1.get("abc"))
print(d1.get("abd"))  # 있으면 value 반환. 없으면 none
print(d1.get("abd", "default"))  # 있으면 value 반환. 없으면 default 반환

d1['apple'] = 'Computer Programming'
d1['abc'] = 'override'
print(d1)

d2 = {'abc': 'alphabet', 'apple': []}
d2['apple'].append('red')
print(d2)
print(d2.keys())
print(d2.values())
print(d2.items())
print(d2.popitem())

# 사전 순서보장 안됨

d2 = {'ㅁㅁ' : '졸려'}
d1.update(d2)
print(d1)

d1[34] = 36
d1[(1,2 )] = (1, 2)  # 튜플 안 쪽에 숫자나 문자만 가능
d1[(1, 2, [1])] = (1, 2)