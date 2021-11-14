# -*- coding: utf-8 -*-
def insertSort(a):
    if len(a) <= 1:
        return a
    for i in range(1, len(a)):
        insert_val = a[i]
        j = i - 1
        while j >= 0:

            if a[j] > insert_val:
                a[j + 1] = a[j]  # 后移给insert_val大哥找位置
            else:
                break
            j -= 1
        a[j + 1] = insert_val
    print(a)


def insert_sort(alist):
    n = len(alist)
    for j in range(0, n):
        for i in range(j, 0, -1):
            if alist[i] < alist[i - 1]:
                alist[i], alist[i - 1] = alist[i - 1], alist[i]
            else:
                break
    print(alist)


def try_angin(arr):
    for i in range(1, len(arr)):  # 要进来排队的人
        j = i - 1  # 在队伍里面的人（比身高排队）
        insert_val = arr[i]
        while j >= 0:
            if arr[j] > insert_val:
                arr[j + 1] = arr[j]
            else:
                arr[j + 1] = insert_val
                break
            j -= 1
    print(arr)


if __name__ == '__main__':
    lists = [3,1,5]
    # insertSort(lists)
    # insert_sort(lists)
    try_angin(lists)
