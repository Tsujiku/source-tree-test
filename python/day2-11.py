l1 = [1, 2, 3, 4, 5]
l1_iter = iter(l1)
print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))
print(next(l1_iter))
# print(next(l1_iter))
#StopIteration

class yrange:
    def __init__(self):
        self.i = 0

    def __iter__(self):
        return self # 반드시 자기 자신을 반환

    def __next__(self):
        if self.i < 5:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration('no more')

yr = yrange()
print(next(yr))
print(next(yr))
print(next(yr))
print(next(yr))
print(next(yr))
print(next(yr))
