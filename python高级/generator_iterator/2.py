# coding=utf-8
def helper(n):
    a = 1
    b = 2
    for _ in range(n):
        a, b = b, a+b
        yield b

if __name__ == '__main__':
    n = 10
    while n > 0:
        n = n//2
        print(n)