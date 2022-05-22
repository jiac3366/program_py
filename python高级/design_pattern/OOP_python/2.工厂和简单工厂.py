# coding=utf-8
from abc import ABCMeta, abstractmethod


# 简单工厂模式
class Popping:
    def dance(self):
        print("popping")


class HipHop:
    def dance(self):
        print("hiphop")


class DanceFactory:
    def start_dance(self, method):
        if method == 'popping':
            return Popping()
        if method == "hiphop":
            return HipHop()


# 工厂模式
class DancingFactory(metaclass=ABCMeta):
    @abstractmethod
    def dancing(self):
        pass


class PoppingFactory(DanceFactory):

    def dancing(self):
        return Popping()

class HipHopFactory(DanceFactory):

    def dancing(self):
        return HipHop()


if __name__ == '__main__':
    p = PoppingFactory()
    pp = p.dancing()
    pp.dance()
