# 모듈 - 파이썬 파일 하나 하나
# namespace 모듈의 이름이 저장됨
# print(__name__)
#
# if __name__ == "__main__":
#     pass
import day21 # as d2 -> alias
from day21 import hello as day21_hello # 함수 뿐만 아니라 변수, 클래스 다 가져올 수 있다

def m_name():
    return __name__


if __name__ == "__main__":
    print(m_name())
    print(day21.m_name())
    print(day21_hello())