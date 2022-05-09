# coding=utf-8

# ======================极客时间=============================
# ，通过__getattribute__和闭包的配合实现，其中有个注意点就是在获取target时不能使用self.target，
# 不然会递归调用self.__getattribute__导致堆栈溢出：
class RealClass(object):
    def realFunc(self, s):
        print(f"Real func is coming {s}")


class DynamicProxy(object):
    def __init__(self, target):
        self.target = target

    def __getattribute__(self, name):
        target = object.__getattribute__(self, "target")
        attr = object.__getattribute__(target, name)

        def newAttr(*args, **kwargs):
            print("Before Calling Func")
            res = attr(*args, **kwargs)
            print("After Calling Func")
            return res

        return newAttr

def main2():
    # 果然是这样 像装饰器啊简直了
    DynamicProxy(RealClass()).realFunc('heihei')



# ====================下面例子和B站[设计模式]一样，其实都是实现了相同的接口===============================
# https://www.cnblogs.com/ydf0509/p/8525970.html
class SensitiveInfo:

    def __init__(self):
        self.users = ['nick', 'tom', 'ben', 'mike']

    def read(self):
        print('There are {} users: {}'.format(len(self.users), ' '.join(self.users)))

    def add(self, user):
        self.users.append(user)
        print('Added user {}'.format(user))


class VirtualInfo:
    """ SensitiveInfo的虚代理"""

    def __init__(self):
        self.virtualInfo = None

    def read(self):
        self.virtualInfo = SensitiveInfo()
        self.virtualInfo.read()

    def add(self, user):
        self.virtualInfo.add(user)


class Info:
    '''SensitiveInfo的保护代理'''

    def __init__(self):
        self.protected = SensitiveInfo()
        self.secret = '0xdeadbeef'

    def read(self):
        self.protected.read()

    def add(self, user):
        sec = input('what is the secret? ')
        self.protected.add(user) if sec == self.secret else print("That's wrong!")


def main():
    info = Info()
    while True:
        print('1. read list |==| 2. add user |==| 3. quit')
        key = input('choose option: ')
        if key == '1':
            info.read()
        elif key == '2':
            name = input('choose username: ')
            info.add(name)
        elif key == '3':
            exit()
        else:
            print('unknown option: {}'.format(key))


if __name__ == '__main__':
    main2()
