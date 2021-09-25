# -*- coding: utf-8 -*-
def func(s):
    rev = [i.lower() for i in s if i.isalnum()]

    rev = "".join(rev)
    print(rev)
    return rev == rev[::-1]


if __name__ == '__main__':
    print(func("A man, a plan, a canal: Panama"))