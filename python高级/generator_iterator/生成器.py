# 斐波那契数列
def gen_fib(index):
    count = 0
    a, b = 0, 1
    while count < index:
        yield b
        a = b,
        b = a + b
        count += 1


# 12.20日有新一波的理解
# 可以自己做一个迭代器：1 自己维护这个index 通过__next__方法返回每一个元素
# 2 用__iter__方法返回这个自己做的迭代器
# 3 如果需要延迟求元素 则就是用yield 每next一次才生成一个值

if __name__ == '__main__':
    for i in gen_fib(10):
        print(i)
