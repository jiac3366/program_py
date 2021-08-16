# -*- coding: utf-8 -*-
def sqrts(x):
    if x == 0 or x == 1:
        return x

    l = 0
    r = x
    ans = -1
    while abs(l - r) < 1e-09:
        mid = (l + r) / 2
        if mid == (x / mid):
            return mid

        if mid > (x / mid):
            r = mid

        if mid <= (x / mid):
            l = mid
            ans = mid
    return ans


if __name__ == '__main__':
    # x = 0.000000000001
    print(sqrts(8))
