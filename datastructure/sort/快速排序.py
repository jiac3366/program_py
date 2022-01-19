import random
import sys
import time


def quick_sort(lists):
    # 基线条件
    if len(lists) < 2:
        return lists
    # 递归条件
    else:
        # 未优化 --30000随机数耗时
        funda = lists[0]  # --以第一个数为基准 --50万条随机数耗时 0.19401860237121582
        small_list = [i for i in lists[1:] if i <= funda]
        large_list = [i for i in lists[1:] if i > funda]
        return quick_sort(small_list) + [funda] + quick_sort(large_list)

        # 以随机数选择貌似对性能提升无益 --50万条随机数耗时 0.2568483352661133
        # 基准元素
        # funda = lists[random.randint(0, len(lists) - 1)]
        # # 基准元素的下标
        # index = lists.index(funda)
        # newlists = lists[:index] + lists[index + 1:]
        # small_list = [i for i in newlists if i <= funda]
        # large_list = [i for i in newlists if i > funda]
        # return quick_sort(small_list) + [funda] + quick_sort(large_list)

        # 取新数组的第一个数 最后一个数 中位数 --50万条随机数耗时 0.2100071907043457
        # lst = [lists[0], lists[-1], lists[int(len(lists) / 2)]]
        # funda = sorted(lst)[1]
        # index = lists.index(funda)
        #
        # newlists = lists[:index] + lists[index + 1:]
        # small_list = [i for i in newlists if i <= funda]
        # large_list = [i for i in newlists if i > funda]
        # return quick_sort(small_list) + [funda] + quick_sort(large_list)


# def quick_sort(lists=[1, 5, 6, 2, 3, 4]):
def quick_sort_new(lists):
    quick_r(lists, 0, len(lists) - 1)
    return lists


def part(lists, p, r):
    i = p
    j = p
    while j < r:
        if lists[j] < lists[r]:
            swap(lists, i, j)
            i += 1
        j += 1
    swap(lists, i, j)
    return i


def swap(lists, i, j):
    tmp = lists[i]
    lists[i] = lists[j]
    lists[j] = tmp


def quick_r(lists, p, r):
    if p >= r:
        return
    q = part(lists, p, r)
    quick_r(lists, p, q - 1)
    quick_r(lists, q + 1, r)


if __name__ == '__main__':
    sys.setrecursionlimit(150000)
    list_num = []
    for i in range(100000):
        list_num.append(random.randint(1, 100000))

    begin = time.time()
    print(quick_sort(list_num))
    end = time.time()
    print(end - begin)
