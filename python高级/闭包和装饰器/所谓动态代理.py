class User:
    def login(self):
        print('user login')

    def logout(self):
        print('user logout')


class Proxy:

    def __init__(self, target):
        self.target = target

    def __getattribute__(self, name):
        target = object.__getattribute__(self, "target")
        attr = object.__getattribute__(target, name)

        if name == 'login':
            def newFunc(*args, **kwargs):
                print("login start")
                result = attr(*args, **kwargs)
                print("login end")
                return result

            return newFunc
        else:
            return attr


if __name__ == '__main__':
    # print(User.__dict__.items())
    # for x, y in User.__dict__.items():
    #     print(x, y)
    # methods = [x  if type(y) == FunctionType]
    # print(globals())

    u = User()
    p = Proxy(u)

    p.login()  # 实际上调用的是动态创建的方法
    p.logout()  # 调用的是原来的方法
