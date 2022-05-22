from abc import ABCMeta, abstractmethod


class Adj(metaclass=ABCMeta):
    @abstractmethod
    def show(self, dance):
        pass


class Dance(metaclass=ABCMeta):
    # 接受参数的一方 需要接纳另外一个人
    def __init__(self, adj):
        self.adj = adj

    @abstractmethod
    def dance(self):
        pass


class Poppin(Dance):
    name = "poppin"

    def dance(self):
        self.adj.show(self)


class Hiphop(Dance):
    name = "hiphop"

    def dance(self):
        self.adj.show(self)


class Cool(Adj):
    def show(self, dance):
        print("炫酷的" + dance.name)


class Ugly(Adj):
    def show(self, dance):
        print("丑陋的" + dance.name)


if __name__ == '__main__':
    Hiphop(Ugly()).dance()
