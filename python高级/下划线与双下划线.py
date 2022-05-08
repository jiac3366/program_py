# coding=utf-8
class A(object):

    def __method(self):
        print("I'm a method in class A")

    def method_x(self):
        print("I'm another method in class A\n")

    def method(self):
        self.__method()
        self.method_x()


class B(A):

    def __method(self):  # 从运行结果来看 它无法重写A的__method
        print("I'm a method in class B")

    def method_x(self):
        print("I'm another method in class B\n")


if __name__ == '__main__':
    print("situation 1:")
    a = A()
    a.method()

    b = B()
    b.method()

    print("situation 2:")
    # b.__method() 报错 'B' object has no attribute '__method'
    a._A__method()
    b._A__method()
    b._B__method()
