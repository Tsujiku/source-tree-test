import time

from functools import wraps

def opt_tracking(use_yn):
    def tracking(func):

        @wraps(func)
        def inner(*args, **kwargs): # 가변 인자를 줄 수 있음
            print(time.ctime())
            if use_yn == "y":
                return func(*args, **kwargs)
            else:
                return "실패"
        return inner # 괄호 절대 안됨
    return tracking


@opt_tracking('n') # 실제 내부 사용을 막기 위해 사용
def hello():
    """hello 함수는 4를 반환합니다"""
    return 4

print(hello)
help(hello)