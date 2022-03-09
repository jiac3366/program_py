class demoClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)  # __new__(): <class '__main__.demoClass'> ('abc',) {}
        instance = super().__new__(cls)  # instance这个东西就是返回给__init__()的self
        instance.number = cls.instances_created  #
        cls.instances_created += 8
        print(cls)       # <class '__main__.demoClass'>
        print(instance)  # <__main__.demoClass object at 0x00000284FEC93E88>  cls和instance 两者不相等
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)  # __init__(): <__main__.demoClass object at 0x00000284FEC93E88> abc
        self.attribute = attribute


test1 = demoClass("abc")
print(test1.number, test1.instances_created)  # 0 8
print(test1.instances_created is demoClass.instances_created)  # True
# 说明：test1的三个属性number、instances_created、attribute，其中instances_created是类属性
pass
