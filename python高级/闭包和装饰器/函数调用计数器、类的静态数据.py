def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func

    return decorate


@static_vars(counter=0)
def foo():
    foo.counter += 1


# 这里使用静态变量目的是在类中实现一个静态的队列，这里用数组实现，任何时候插入到队列中的数据不会和类的实例有直接关系

class CaptchaImage:
    def queue(self, arr=list()):
        return arr

    def InsertCode(self, code):
        self.queue().append(code)


if __name__ == '__main__':
    foo()
    foo()
    foo()
    foo()
    foo()
    print(foo.counter)
    c = CaptchaImage()
    c.InsertCode(1)
    b = CaptchaImage()
    b.InsertCode(2)
    print(b.queue())
    print(c.queue())
