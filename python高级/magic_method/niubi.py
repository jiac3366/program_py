# coding=utf-8
class C:
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        # print(1, object.__getattribute__(self, *args, **kwargs))
        return object.__getattribute__(self, *args, **kwargs)

    def __getattr__(self, name):
        print("__getattr__() is called")
        return name + " from getattr"

    def __get__(self, instance, owner):
        print("__get__() is called", instance, owner)  # instance 是访问desciptor的实例
        return self

    def foo(self, x):
        print(x)

    def __call__(self, *args, **kwargs):
        print('__call__() is called', args, kwargs)


class C2:
    d = C()


if __name__ == '__main__':
    c = C()
    c2 = C2()
    print(c.a)  # 1、__getattribute__() is called 2、abc  先调用__getattribute__()方法，然后获取属性
    print(c.zzzzzzzz)  # 1、__getattribute__() is called 2、__getattr__() is called 3、zzzzzzzz from getattr
    print(c2.d)  # d是C类的实例，而C因为存在__get__()方法，而变成描述符，访问文件描述符的实例的时候，默认应该是不走__getattribute__方法，所以也就更不可能调用到__getattr__()方法
    # 1、__get__() is called 2、C2 object 3、C2 4、d指向的实例C object
    print('//////////////////////////////////')
    print(c2.d.a)  # 同上面一样会先获取d，走__get__()方法，然后获取a属性的时候又会走__getattribute__
    # 1、__get__() is called 2、C2 object 3、C2 4、__getattribute__ 5、abc
    print('..................................')
    print(c2.d.b)  # 继续上面的逻辑，是描述符，到获取b属性，没有找到走__getattr__()方法返回
    # 1、__get__() is called 2、C2 object 3、C2 4、__getattribute__ 5、__get__ 6、b from getattr
    print('----------------------------------')
    print(c())  # 实例本身调用是调用的call方法
    print('**********************************')
    print(c.c)  # 非文件描述符的还是老思路 getattribute==>getattr
    # 1、__getattribute__ 2、__getattr__ 3、c from getattr__getitem__.py
