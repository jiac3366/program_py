# coding=utf-8

class Goods:
    """经典类，具有一种@property装饰器"""

    @property
    def price(self):
        return "laowang"


# ############### 调用 ###############
obj = Goods()
result = obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
print(result)


class Goods:
    """python3中默认继承object类
        以python2、3执行此程序的结果不同，因为只有在python3中才有@xxx.setter  @xxx.deleter
    """

    @property
    def price(self):
        print('@property')

    @price.setter
    def price(self, value):
        print('@price.setter')

    @price.deleter
    def price(self):
        print('@price.deleter')


if __name__ == '__main__':
    obj = Goods()
    obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
    obj.price = 123  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
    del obj.price  # 自动执行 @price.deleter 修饰的 price 方法
