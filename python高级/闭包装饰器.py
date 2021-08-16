# 调用函数的参数会少很多--因为有一部分已经传进去了
# 写法会比普通函数更加优雅
import time
import random


# 通常情况下，我们会把*args和**kwargs，作为装饰器内部函数 wrapper() 的参数, 表示接受任意数量和类型的参数
def compute(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("my decorator")
        print("operate time is " + str(end - start))
    return wrapper


@compute
def hello(strs):
    print(strs)
    print("hello")


def partition(lists, start, end):
    """寻找出中轴的下标"""
    # 犯错3
    # if start >= end:
    #     return
    # 犯错4
    # remark = 0
    remark = start
    # 犯错2
    # middle = lists[0]
    middle = lists[start]
    # 犯错5
    # for i in range(len(lists)):
    for i in range(start + 1, end + 1):
        # 犯错6
        # if i < middle:
        if lists[i] < middle:
            remark += 1
            temp = lists[remark]
            # 犯错7
            # lists[remark] = lists[middle]
            lists[remark] = lists[i]
            lists[i] = temp
    lists[start] = lists[remark]
    lists[remark] = middle
    return remark


@compute
def quicksort(lists, start, end):
    if start >= end:
        return
    # 犯错1
    # mid = partition(lists, start, len(lists)-1)
    mid = partition(lists, start, end)
    quicksort(lists, start, mid - 1)
    quicksort(lists, mid + 1, end)


if __name__ == '__main__':
    # 普通写法：compute(hello)是一个函数
    hello("aaa")
    # 装饰器写法 @compute
    # lists = [random.randint(1, 100000) for i in range(3000)]
    # quicksort(lists, 0, len(l   ists) - 1)
