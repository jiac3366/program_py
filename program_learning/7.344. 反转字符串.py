# -*- coding: utf-8 -*-
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """

    n = len(s)
    i = 0
    while i < n / 2:
        temp = s[n - i - 1]
        s[n - i - 1] = s[i]
        s[i] = temp
        i += 1

    return s


if __name__ == '__main__':
    print(reverseString(["h", "e", "l", "l", "o"]))
