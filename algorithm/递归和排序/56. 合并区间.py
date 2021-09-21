# -*- coding: utf-8 -*-

def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """

    merge = []
    if len(intervals) == 1:
        return intervals
    merge.append(intervals[0])
    intervals.pop(0)
    for item in intervals:
        if item[0] > merge[len(merge) - 1][1]:
            merge.append(item)
        else:
            merge[len(merge) - 1][1] = item[1]
    print(merge)
    return merge


if __name__ == '__main__':
    merge([[1, 4], [2, 6], [8, 10], [15, 18]])
    lista = [[1, 4], [2, 6], [8, 10], [15, 18]]

    print(sorted(lista, key=lambda x: x[0]))
