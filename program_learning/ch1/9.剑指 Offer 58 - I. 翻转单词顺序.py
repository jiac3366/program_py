# -*- coding: utf-8 -*-
def reverseWords(s: str):
    # 先写trim() 把"  a good   example  "=>"a good example"
    # 再写出swap() 对每一个word都原地执行一次swap()
    # 空间复杂度为O(1)

    s = [item for item in s]

    n = trim(s)
    if n == 0: return ""

    print(n)
    swap(s, 0, n - 1)
    print(s)
    p = 0
    while p < n:
        r = p
        while r < n and s[r] != " ":
            r += 1
        swap(s, p, r - 1)
        p = r + 1
    print(s)

    new_s = []
    for i in range(n):
        new_s.append(s[i])
    return "".join(new_s)


# ???????????????????????????????????????????????????????????
def swap(s, p, r):
    mid = (p + r) / 2
    i = p
    while i < mid:
        temp = s[i]
        s[i] = s[r - i + p]
        s[r - i + p] = temp
        i += 1


def trim(s):
    k = i = 0
    n = len(s)

    print(s)
    while i < n and s[i] == " ":
        i += 1
    while i < n:
        if s[i] != " ":
            s[k] = s[i]
            k += 1
        else:
            if i + 1 < n and s[i + 1] != " ":
                s[k] = " "
                k += 1
        i += 1
    print(s)
    # k后面的要截掉
    # return "".join(s[:k])
    return k


if __name__ == '__main__':
    s = "the sky is blue"

    print(reverseWords(s))
