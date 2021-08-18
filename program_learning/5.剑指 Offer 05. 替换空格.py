# -*- coding: utf-8 -*-
def replaceSpace(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ""
    string = ["" for _ in range(3*len(s))]
    index = 0
    for i in s:
        if i == " ":
            string[index] = "%"
            index += 1
            string[index] = "2"
            index += 1
            string[index] = "0"
            index += 1
        else:
            string[index] = i
            index += 1
    return "".join(string)


if __name__ == '__main__':
    print(replaceSpace("     "))

