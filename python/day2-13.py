# generator
def foo():
    print("begin")
    for i in range(3):
        print("before", i)
        yield i
        print("after", i)
    print("end")

for item in foo():
    print("{}: from foo".format(item))

# 많은 양의 데이터를 처리할 때