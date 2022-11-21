class A:
    def __get__(self, instance, owner=None):
        if not instance:
            pass
            return self
        return "is instance"

    def __set__(self, instance, value):
        pass


class B:
    a = A()


if __name__ == '__main__':
    b = B()
    b.a = 22
