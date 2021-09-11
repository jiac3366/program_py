class A(object):
    bar = 1

    def normal_method(self, name):
        print('normal_method')

    @staticmethod
    def static_method():
        print('static_method')
        # 静态方法可以调用类属性 但是为啥博客说不可以调用
        print(A.bar)

    @classmethod
    def class_method(cls):
        print('class_method')
        print(cls.bar)
        # 实例调用实例方法
        cls().normal_method("normal")


if __name__ == '__main__':
    pass
    # 1. 类不能直接调用实例方法
    # A.normal_method() # 报错

    # 2. 类可以调用静态方法和类方法
    # A.static_method()
    # A.class_method()

    # 3. 类实例3个都可以调用,因为类方法传入了cls隐含参数，其实相当于self
    # a = A()
    # a.normal_method()
    # a.static_method()
    # a.class_method()

    # https://www.cnblogs.com/jayliu/p/9030725.html
    # 4.实例方法（普通方法）——————————————————————随着实例属性的改变而改变
    #
    # 类方法（无论是类调用还是实例调用）————————————都是类属性的值，不随实例属性的变化而变化
    #
    # 静态方法————————————————————————————不可以访问类属性，故直接输出传入方法的值
