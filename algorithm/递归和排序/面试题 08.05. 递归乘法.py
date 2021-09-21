# -*- coding: utf-8 -*-
def multiply(A: int, B: int) -> int:
    res = 0

    def helper(A, B):
        if A == 1:
            return B

        res = B + helper(A - 1, B)
        return res

    if A > B:
        return helper(B, A)
    return helper(A, B)


if __name__ == '__main__':
    print(multiply(3, 4))
