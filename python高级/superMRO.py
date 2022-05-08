# coding=utf-8
# coding=utf-8
# 实例一：
class A(object):
    def __init__(self):
        print("class ---- A ----")


class B(A):
    def __init__(self):
        print("class ---- B ----")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("class ---- C ----")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print(D.__mro__)
        print("class ---- D ----")
        super(C, self).__init__()  # super(B, self).__init__()仍然会按照print(D.__mro__)的顺序进行打印


d = D()
'''
#输出结果：
class ---- D ----
class ---- B ----
class ---- C ----
class ---- A ----
'''
