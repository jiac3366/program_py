# -*- coding: utf-8 -*-


def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []

    s = s.strip()
    i = j = len(s) - 1

    while i >= 0:
        while i >= 0 and s[i] != ' ': # 这里一定要加i >= 0 不是啰嗦，而是s[-1]是字符串最后一个字母
            i -= 1
        stack.append(s[i + 1: j + 1])

        while s[i] == ' ': # 因为上面while结束的原因是i=-1 已经到头 没必要再去除空格
            i -= 1
        j = i
        pass


if __name__ == '__main__':
    string = "the sky is blue"
    print(reverseWords(string))
