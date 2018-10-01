# 데코레이터
import time

def tracking(func):
    def inner():
        print(time.ctime())
        return func()
    return inner # 괄호 절대 안됨

@tracking # tracking 먼저 실행
def hello():
    return 4

print(hello())
print(hello)

# 다른 함수 시작 전에 해야할 일을 적음 - 데코레이터
# 한빛 미디어 - 데코레이터 검색 글 관련 article 있음


