def adder():
    sum = 0

    def f(i):
        nonlocal sum
        sum = sum + i
        return sum

    return f


if __name__ == '__main__':
    a = adder()
    for i in range(1,11):
        print("sum %d" % a(i))