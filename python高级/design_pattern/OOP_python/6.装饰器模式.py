# 可以对原始类嵌套使用多个装饰器。为了满足这个应用场景，在设计的时候，装饰器类需要跟原始类继承相同的抽象类或者接口
# 下面是正儿八经的的支持任何面向对象语言的写法。python还有独有的@形式的装饰器
class Foo(object):
    def f1(self):
        print("original f1")

    def f2(self):
        print("original f2")


class Foo_decorator(object):
    def __init__(self, decoratee):
        self._decoratee = decoratee

    def f1(self):
        print("decorated f1")
        self._decoratee.f1()

    def __getattr__(self, name):
        return getattr(self._decoratee, name)


u = Foo()
v = Foo_decorator(u)
v.f1()
v.f2()


# 使用python特有的装饰器写法
# coding=utf-8

def decorator(func):
    def _inner(*args, **kwargs):
        print
        '在前面加点东西'
        func(*args, **kwargs)
        print
        '在后面加点东西'

    return _inner


@decorator
def f1(a):
    print
    a


f1(5)
