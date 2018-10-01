import time

from functools import wraps

def tracking(func):

    @wraps(func)
    def inner(): # 가변 인자를 줄 수 있음
        print(time.ctime())
        return func()
    return inner # 괄호 절대 안됨

@tracking # tracking 먼저 실행
def hello():
    """hello 함수는 4를 반환합니다"""
    return 4

print(hello)
help(hello)