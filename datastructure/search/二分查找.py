list_num = [1, 2, 2, 2, 3, 4]
"""
Author:Jiac
Date:2021.4.27
"""


def binary_search(lists, item):
    low = 0
    high = len(lists) - 1

    while low <= high:
        mid = low + (high - low) // 2
        guess = lists[mid]
        if item == guess:
            return mid
        elif item > guess:
            low = mid + 1
        elif item < guess:
            high = mid - 1
    return -1


def left_binary_search(lists, item):
    low = 0
    high = len(lists)
    while low < high:
        mid = low + (high - low) // 2
        if item == lists[mid]:
            high = mid
        elif item < lists[mid]:
            high = mid
        elif item > lists[mid]:
            low = mid + 1
    return low


def right_binary_search(lists, item):
    low = 0
    high = len(lists)
    while low < high:
        mid = low + (high - low) // 2
        if item == lists[mid]:
            low = mid + 1
        elif item < lists[mid]:
            high = mid
        elif item > lists[mid]:
            low = mid + 1
    # 因为left = right是while终止的条件
    # 又因为我们返回的肯定是mid 但是终止前缺神奇地加了一次：“low = mid + 1”
    # 所以我们要返回mid = low - 1
    return low - 1


if __name__ == '__main__':
    print(list_num)
    print(right_binary_search(list_num, 2))
