# -*- coding: utf-8 -*-
import functools

def decorate(func):
    def wrapper(*args, **kwargs):
        print('==========2========')
        func(*args, **kwargs)
        print('========2==========')

    return wrapper


def repeat(num):
    def decorate(func):
        # 将原函数的元信息，拷贝到对应的装饰器函数里
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num):
                print('==================')
                func(*args, **kwargs)
                print('==================')

        return wrapper

    return decorate


@decorate
def hello(name):
    print('say,hello', name)


# 不同函数要穿不同个数的参数
@decorate
def hello2(name, yes):
    print('say,hello', name, yes)


# 传参数到装饰器
@repeat(4)
def hello3(name, yes):
    print('say,hello', name, yes)


if __name__ == '__main__':
    decorate(hello)
