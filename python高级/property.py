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


# ========================================================
class Goods2:
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


# if __name__ == '__main__':
#     obj = Goods2()
#     obj.price  # 自动执行 @property 修饰的 price 方法，并获取方法的返回值
#     obj.price = 123  # 自动执行 @price.setter 修饰的 price 方法，并将  123 赋值给方法的参数
#     del obj.price  # 自动执行 @price.deleter 修饰的 price 方法

# ========================================================

class Goods3(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    @property
    def price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    @price.setter
    def price(self, value):
        self.original_price = value

    @price.deleter
    def price(self):
        del self.original_price


# if __name__ == '__main__':
#     obj = Goods3()
#     print(obj.price)  # 获取商品价格
#     obj.price = 200  # 修改商品原价
#     print(obj.price)
#     del obj.price  # 删除商品原价
#     print(obj.price)


# ========================================================

class Foo:
    def get_bar(self):
        return 'laowang'

    BAR = property(get_bar)


obj = Foo()
reuslt = obj.BAR  # 自动调用get_bar方法，并获取方法的返回值
print(reuslt)


# ========================================================


class Foo(object):
    def get_bar(self):
        print("getter...")
        return 'laowang'

    def set_bar(self, value):
        """必须两个参数"""
        print("setter...")
        return 'set value' + value

    def del_bar(self):
        print("deleter...")
        return 'laowang'

    BAR = property(get_bar, set_bar, del_bar, "description...")


obj = Foo()

obj.BAR  # 自动调用第一个参数中定义的方法：get_bar
obj.BAR = "alex"  # 自动调用第二个参数中定义的方法：set_bar方法，并将“alex”当作参数传入
desc = Foo.BAR.__doc__  # 自动获取第四个参数中设置的值：description...
print(desc)
del obj.BAR  # 自动调用第三个参数中定义的方法：del_bar方法


# ========================================================

class Goods(object):

    def __init__(self):
        # 原价
        self.original_price = 100
        # 折扣
        self.discount = 0.8

    def get_price(self):
        # 实际价格 = 原价 * 折扣
        new_price = self.original_price * self.discount
        return new_price

    def set_price(self, value):
        self.original_price = value

    def del_price(self):
        del self.original_price

    PRICE = property(get_price, set_price, del_price, '价格属性描述...')

if __name__ == '__main__':

    print("---------")
    obj = Goods()

    print(obj.PRICE)  # 获取商品价格
    obj.PRICE = 200  # 修改商品原价
    print(obj.PRICE)

    del obj.PRICE  # 删除商品原价
