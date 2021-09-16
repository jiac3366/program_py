# -*- coding: utf-8 -*-


# "123" "12 3" "123 " "2db", "288"
def _check_seg(seg):
    # 处理None
    if not seg:
        return False

    # # 处理是否0~255
    index = 0
    n = len(seg)
    # s = ""
    # while index < len(seg) and seg[index] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
    #     # 处理0~255
    #     s += seg[index]
    #     if not 0 < int(s) < 255:
    #         return False
    #     else:
    #
    #     index += 1

    while index < n and seg[index] == " ":
        index += 1
    # 处理全是空格
    if index == n:
        return False

    # 处理前面的数字部分
    # index = 0  不能重置为0 因为数字段前面允许有空格
    digits = ""
    while index < n and seg[index] != " ":
        # 将是数字的字母拼接起来
        # 处理非数字
        if not 48 <= ord(seg[index]) <= 57:
            return False
        digits += seg[index]
        # 处理0~255
        if int(digits) > 255:
            return False
        index += 1
    # index = 0  这里不能重置为0 继续往下走
    # 后面如果还有非空格 就说明ip数字段的中间有空格 '12 3'
    while index < n:
        if seg[index] != " ":
            return False
        index += 1

    return True


def IP_parser(string):
    # 分成四段
    seg_list = string.split(".")
    if len(seg_list) != 4:
        return False

    # 对每段进行处理
    for seg in seg_list:
        res = _check_seg(seg)
        if not res:
            return False
    return True


if __name__ == '__main__':
    # 测试用例
    # 192.92.2.34  # 合法
    # 192 . 52.21. 1

    # 300.54.55.11  # 不合法
    # 2ff.55.23.66
    # 2 .5 6.74.1
    # 12..63.2
    # 232. 33 . 22
    # "  "
    # None
    print(IP_parser("None"))
