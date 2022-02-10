class demoClass:
    instances_created = 0

    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)  # __new__(): <class '__main__.demoClass'> ('abc',) {}
        instance = super().__new__(cls)  # 这个东西就是self
        instance.number = cls.instances_created
        cls.instances_created += 8
        print(cls)  # <class '__main__.demoClass'>
        print(instance)  # <__main__.demoClass object at 0x00000284FEC93E88>  两者!=
        return instance

    def __init__(self, attribute):
        print("__init__():", self, attribute)  # __init__(): <__main__.demoClass object at 0x00000284FEC93E88> abc
        self.attribute = attribute


test1 = demoClass("abc")
print(test1.number, test1.instances_created)  # 0 8
print(test1.instances_created is demoClass.instances_created)  # True说明：test1的三个属性 其中有一个是类属性
