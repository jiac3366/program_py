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

                break
            j -= 1

        arr[j + 1] = insert_val
    print(arr)

def try_agin2(A):
    x = 1
    while x < len(A):
        y = x - 1
        insert_num = A[x]
        while y >= 0 and insert_num < A[y]:
            A[y+1] = A[y]
            y -= 1
        A[y+1] = insert_num
        x += 1
    return A



if __name__ == '__main__':
    lists = [4, 5, 6, 1, 3, 2]
    print(try_agin2(lists))
    # insert_sort(lists)
