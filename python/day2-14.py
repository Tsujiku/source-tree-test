# Exception Handling
l1 = [1, 2, 3]

try:
    print(l1[3]) # 에러 발생
    # 7 / 0
except (IndexError, ZeroDivisionError) as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print('에러 발생하거나 말거나 끝나고 해야할 일')


def foo():
    try:
        7/0
    except ZeroDivisionError as e:
        raise e # 호출한 측에 알려주어야 함

foo()

def goo():
    raise KeyError('dd')

goo()