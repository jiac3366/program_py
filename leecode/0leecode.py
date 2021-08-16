# a b c d e f a b d -> c
from collections import Counter
import functools
import time


# 快捷键
# Ctrl + Shift + ← / → ：    光标向左/向右选中一个单词
# Shift + Home/End：光标从当前位置一直选中到行首/尾
# Ctrl + ← / → ：    光标向左/向右跳转一个单词
# Ctrl + Backspace / Delete ：    光标向左/向右删除一个单词
def compute(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print("operate time is " + str(end - start))

    return wrapper


@functools.lru_cache(None)
def climbStairs(n):
    if n < 0:
        return
    if n < 3:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)


if __name__ == '__main__':
    start = time.time()
    print(climbStairs(66))
    end = time.time()
    print("operate time is " + str(end - start))
