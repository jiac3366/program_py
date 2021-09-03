# -*- coding: utf-8 -*-
import array
def trim(s):
    k = i = 0
    n = len(s)

    s = [item for item in s]
    print(s)
    while s[i] == " ":
        i += 1
    while i < n:
        if s[i] != " ":
            s[k] = s[i]
            k += 1
        else:
            if i+1 < n and s[i + 1] != " ":
                s[k] = " "
                k += 1
        i += 1
    print(s)
    # k后面的要截掉
    return "".join(s[:k])


if __name__ == '__main__':
    print(trim("     hehe  apple   iphone"))
