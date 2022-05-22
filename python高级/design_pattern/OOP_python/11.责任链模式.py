# coding=utf-8
from abc import ABCMeta, abstractmethod

# 抽象的处理者
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        pass

# 具体的处理者
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 30:
            print('总经理准假%d' % day)
        else:
            print('可以辞职了！')

# 具体的处理者
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print('项目主管准假%d' % day)
        else:
            print('部门经理职权不足')
            self.next.handle_leave(day)

# 具体的处理者
class ProjectDirector(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print('项目主管准假%d' % day)
        else:
            print('项目主管职权不足')
            self.next.handle_leave(day)

day = 20
p = ProjectDirector()
p.handle_leave(day)
"""
项目主管职权不足
部门经理职权不足
总经理准假20
"""