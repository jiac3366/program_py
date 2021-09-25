# -*- coding: utf-8 -*-


def strToInt(str):
    """
    :type str: str
    :rtype: int
    """
    # "   "
    nums_str = str.strip()
    if not nums_str:
        return 0
    frist = nums_str[0]
    if frist != '-' and frist != '+' and not frist.isdigit():
        return 0

    # not negetive 从当前位置开始取整数
    if frist != '-' and frist != '+':
        res = get_int(nums_str, 0)
    else:
        res = get_int(nums_str, 1)
    return res


def get_int(nums_str, begin):
    string = 0
    MAX_NUM = 2 ** 31 - 1
    MIN_NUM = -(2 ** 31)
    for s in nums_str[begin:]:
        if not s.isdigit():
            break
        string = string * 10 + (ord(s) - ord('0'))

    # 负数
    if nums_str[0] == '-':
        string = 0 - string
        if string <= MIN_NUM: return MIN_NUM
    else:
        if string >= MAX_NUM: return MAX_NUM
    return string


if __name__ == '__main__':
    print(strToInt("-91283472332"))
    # print(ord('9'))
