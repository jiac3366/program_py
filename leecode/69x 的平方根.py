def pow(x):
    l, r = 0, x
    res = -1
    while l <= r:
        mid = (l + r) / 2
        if mid * mid == x:
            return mid
        elif mid * mid > x:
            r = mid
        elif mid * mid < x:
            l = mid
            res = mid
    return res


if __name__ == '__main__':
    print(pow(5))
