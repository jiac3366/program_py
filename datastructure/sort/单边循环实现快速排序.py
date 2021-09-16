import random


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


def quicksort(lists, start, end):
    if start >= end:
        return
    # 犯错1
    # mid = partition(lists, start, len(lists)-1)
    mid = partition(lists, start, end)
    quicksort(lists, start, mid - 1)
    quicksort(lists, mid + 1, end)


if __name__ == '__main__':
    list_num = [random.randint(1, 100000) for i in range(3000)]
    print(list_num)

    quicksort(list_num, 0, len(list_num) - 1)
    print(list_num)
