# -*- coding: utf-8 -*-


def getRow(rowIndex):
    """
    :type rowIndex: int
    :rtype: List[int]
    """
    # 解题说明：最好画一下图找规律 不然注释再好 也难以看明白
    res = [0 for i in range(rowIndex + 1)]

    res[0] = 1

    # 外层任务是给首尾置位1 注意观察 下标为i的行的下标为i的元素就是这行的最后一个元素
    # 下标为0的行就只有一个1  我们从下标为1的行开始外循环
    # 求下标为rowIndex的行 外循环要循环3次（看图看出来的555）
    for i in range(1, rowIndex + 1):
        # 内层循环就是从最后1个推到第1个，看图可以看出rowIndex-1就是最后一个元素
        res[0] = res[i] = 1
        for j in range(i - 1, 0, -1):
            res[j] = res[j] + res[j - 1]
    print(res)


if __name__ == '__main__':
    getRow(3)
