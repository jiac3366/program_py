# coding=utf-8

...
# 比如：插入日志、性能测试、事务处理、缓存、权限校验等场景，装饰器是解决这类问题的绝佳设计

import functools


def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):  # 如果用户处于登录状态
            return func(*args, **kwargs)  # 执行函数post_comment()
        else:
            raise Exception('Authentication failed')

    return wrapper


@authenticate
def post_comment(request, ...)
    ...


# =======================================


import time
import functools


def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res

    return wrapper


@log_execution_time
def calculate_similarity(items):
    ...


# ================================

import functools


def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ...  # 检查输入是否合法


@validation_check
def neural_network_training(param1, param2, ...):
    ...


# =========================
# 正确使用缓存装饰器，往往能极大地提高程序运行效率。大型公司服务器端的代码中往往存在很多关于设备的检查
# 如你使用的设备是安卓还是iPhone，版本号是多少。这其中的一个原因，就是一些新的feature，往往只在某些特定的手机系统或版本上才有。
# 我们通常使用缓存装饰器，来包裹这些检查函数，避免其被反复调用，进而提高程序运行效率，


@lru_cache
def check(param1, param2, ...)  # 检查用户设备类型，版本号等等
    ...
