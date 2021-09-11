# -*- coding: utf-8 -*-
def isValid(s: str) -> bool:
    if len(s) % 2 != 0: return False
    stack = []
    left = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for i in s:
        if i in left:
            cur = stack.pop()
            if cur != left[i]:
                return False
        else:
            stack.append(i)

    return stack == []


if __name__ == '__main__':
    print(isValid('}{'))
