print("**********정수형 사칙연산**********")

i1 = 6
i2 = 8

print(i1 + i2)
print(i1 - i2)
print(i1 * i2)
print(i1 / i2)
print(i2 / i1)
print(i2 // i1)
print(i2 % i1)
print(i1 % i2)

print("**********실수형 사칙연산**********")

i1 = 6.4
i2 = 8.5

print(i1 + i2)
print(i1 - i2)
print(i1 * i2)
print(i1 / i2)
print(i2 / i1)
print(i2 // i1)
print(i2 % i1)
print(i1 % i2)

print("**********복소수형 사칙연산**********")

i1 = 6j
i2 = 8j

print(i1 + i2)
print(i1 - i2)
print(i1 * i2)
print(i1 / i2)
print(i2 / i1)
# print(i2 // i1)
# print(i2 % i1)
# print(i1 % i2)

print("**********문자열**********")

s0 = ""
# print("0")
s1 = "abc"
print(s1[0])
print(s1[1])
print(s1[2])

s2 = "Hello developer world"
print(s2[0:10:2])

s3 = "Hello %s world"
print(s3 % "YM")  # python 권장 사항이 아님

s3 = "Hello %s world %s"
print(s3 % ("YM", "!"))  # python 권장 사항이 아님

s3 = "Hello {}{} world"
print(s3.format("cho", " YM"))  # python 권장

s3 = "Hello {1}{0} world"
print(s3.format(" cho", "YM"))  # python 권장

s = "It\'s \"YM\""
print(s)

s = "How" \
    " Are" \
    " You?"
print(s)

s = ("I'm\n"
     "fine\n"
     "thanks")
print(s)

s = """oh oh oh oh oh oh
oh oh oh oh oh oh
oh oh oh oh oh oh"""
print(s)

# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
s = "hello python"
print(s.center(60))
print(s.center(60, '*'))
print(s.count('l'))  # 문자열 안에 l이 몇개 존재하는지
print(s.startswith("h"))
print(s.startswith("H"))
print(s.endswith("n"))
print(s.endswith("N"))

s = "hello python"

print(s.find("python"))  # 문자열에 p가 시작되는 위치를 반환함. 찾지 못하면 -1 반환
print(s.index("python"))  # 문자열에 p가 시작되는 위치를 반환함. 찾지 못하면 error 발생

print(s.find("python", 0, 7))  # 0 부터 7 사이의 python 을 찾음

print(s.rfind("python", 0, 7))  # 뒤부터 찾음
print(s.rindex("python"))  # 뒤부터 찾음

s = "1234"
print(s.isdecimal())  # 10진수인지 아닌지
s = "\N{KHAROSHTHI DIGIT THREE}"
print(s)  # 10진수인지 아닌지

s = "\n{WON SIGN}"
print(s)
s = "\u10A1C"
print(s)

s = "안녕하세요"
print(s.isalnum())

s = "a"
print(s.islower())
print(s.upper())  # 대문자로 바꿔줌
print(s.isspace())  # space tab \n 을 확인

s = "   b     "
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s = "*****b***********"
print(s.strip('*'))
print(s.strip('* '))

s = "*******a*******a****a**"
print(s.replace("a", "b", 2))

money = "13500"
print("최종금액:" + money.zfill(10))

money = 13500
print("최종금액:" + "{:*>10}".format(money))
print("최종금액:" + "{: >10}".format(money))
print("최종금액:" + "{:#,}".format(money))

s = "Alpha"
print(s.casefold())  # 대소문자의 구분을 없애줌. 그러나 lower 랑 다름

