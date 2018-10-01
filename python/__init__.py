from . import pkg1  # 현재 패키지 내부 모듈을 가져오겠다는 의미 . 은 나, .. 은 부모
from . import pkg2
from .pkg1 import pkgf1  # 함수 바로 가져옴


def hello():
    return 4
