# coding=utf-8
# class Foo:
#     def __init__(self, n):
#         self.n = n
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.n < 13:
#             self.n += 1
#             return self.n
#         else:
#             raise StopIteration
#
#
# f1 = Foo(10)
# for i in f1:
#     print(i)
#
#
# # for函数会帮忙捕捉异常并终止循环不会报错。如果采用f1.__next__()方法获得下一个值则在最后一个值位置会报错
#
# # ========================================
# class Fib:
#     def __init__(self, start1, start2):
#         self.start1 = start1
#         self.start2 = start2
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.start1, self.start2 = self.start2, self.start1 + self.start2
#         return self.start2
#
#
# f1 = Fib(1, 2)
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())
# print(f1.__next__())

# =======================================

# _*_coding:utf-8_*_
class Foo:
    def __init__(self, start, stop):
        self.num = start
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.num >= self.stop:
            raise StopIteration
        n = self.num
        self.num += 1
        return n


f = Foo(1, 5)
from collections.abc import Iterable, Iterator

print(isinstance(f, Iterator))

for i in Foo(1, 5):
    print(i)


# ===========================================
# 简单模拟range，加上步长
class Range:
    def __init__(self, n, stop, step):
        self.n = n
        self.stop = stop
        self.step = step

    def __next__(self):
        if self.n >= self.stop:
            raise StopIteration
        x = self.n
        self.n += self.step
        return x

    def __iter__(self):
        return self


for i in Range(1, 7, 3):  #
    print(i)


# =========================================
class Fib:
    def __init__(self):
        self._a = 0
        self._b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self._a, self._b = self._b, self._a + self._b
        return self._b


print("------------------------------")
f1 = Fib()

print(f1.__next__())
print(next(f1))
print(next(f1))

for i in f1:
    if i > 100:
        break
    print('%s ' % i, end='')
