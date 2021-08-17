# -*- coding: utf-8 -*-

# 将192.168.33.44转化成192[.]168[.]33[.]44

def func1(string):
    return string.replace(".", "[.]")


def func2(string):
    newstring = []
    for s in string:
        if s == ".":
            s = "[.]"
        newstring.append(s)
    return "".join(newstring)


if __name__ == '__main__':
    # print(func2("192.168.33.44"))
    dicts = {"1": 2, "3": 66}
    for value, key in enumerate(dicts):
        print(value, key)
    print("3" in dicts)