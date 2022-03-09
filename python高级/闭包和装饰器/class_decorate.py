# -*- coding: utf-8 -*-

class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0   # num_calls这个变量是类变量

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello world")

if __name__ == '__main__':
    example()
    pass

# # 输出
# num of calls is: 1
# hello world
#
    example()
#
# # 输出
# num of calls is: 2
# hello world

