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


if __name__ == '__main__':
    lists = [4, 5, 6, 1, 3, 2]
    insertSort(lists)
    insert_sort(lists)
