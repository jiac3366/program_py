# coding=utf-8
class ObjectDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  # 继承父类dict的构造方法

    def __getattr__(self, name):
        value = self[name]  # self ==> {'asf': {'a': 1}, 'd': True}
        if isinstance(value, dict):
            value = ObjectDict(value)
        return value


class WidgetShowLazyLoad:
    app = "jiac"

    def __init__(self):
        self.add = "chase"

    def fetch_complex_attr(self, attrname):
        return attrname

    def __getattr__(self, name):
        if name not in self.__dict__:  # 没在__dict__字典内找到key
            self.__dict__[name] = self.fetch_complex_attr(name)  # 添加attribute键值对
        return self.__dict__[name]


# if __name__ == '__main__':
#     od = ObjectDict(asf={'a': 1}, d=True)  # 实例化对象od ==>  {'asf': {'a': 1}, 'd': True}
#     print(od.asf)  # {'a': 1}
#     print(od.asf.a)  # 1
#     print(od.d)  # True

# if __name__ == '__main__':
#     w = WidgetShowLazyLoad()
#     print(WidgetShowLazyLoad.__dict__)
#     print('before', w.__dict__)  # 刚开始实例化的时候，__dict__是空的字典
#     w.lazy_loaded_attr  # 属性查找，没找到，调用__getattr__方法
#     print('after', w.__dict__)  # {'lazy_loaded_attr': 'lazy_loaded_attr'}


import functools


class lazy_attribute:
    """ A property that caches itself to the class object. """

    def __init__(self, func):
        functools.update_wrapper(self, func, updated=[])
        self.getter = func  # complex_attr_may_not_need

    def __get__(self, obj, cls):  # 调用类本身， obj自身调用为空
        value = self.getter(cls)  # complex_attr_may_not_need(Widget)
        setattr(cls, self.__name__,
                value)  # self ==> complex_attr_may_not_need=lazy_attribute(complex_attr_may_not_need)
        # self 所以是lazy_attribute的对象，装饰器的原理就是complex_attr_may_not_need=lazy_attribute实例化对象，所以self.__name__就是complex_attr_may_not_need
        # {'complex_attr_may_not_need': 332833500}
        return value


class Widget:
    @lazy_attribute  # complex_attr_may_not_need=lazy_attribute(complex_attr_may_not_need)
    def complex_attr_may_not_need(clz):
        print('complex_attr_may_not_need is needed now')
        return sum(i * i for i in range(1000))


if __name__ == '__main__':
    print(Widget.__dict__.get('complex_attr_may_not_need'))  # <__main__.lazy_attribute object at 0x02B12450>
    Widget.complex_attr_may_not_need  # complex_attr_may_not_need is needed now
    print(Widget.__dict__.get('complex_attr_may_not_need'))  # 332833500
