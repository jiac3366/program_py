from abc import ABCMeta, abstractmethod


# 抽象的订阅者
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        """
        :param notice: Notice类的对象
        :return:
        """
        pass


# 抽象的发布者：可以是接口，子类不需要实现，所以不需要定义抽象方法！
class Notice:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def detach(self, obs):
        self.observers.remove(obs)

    def notify(self):
        """
        推送
        :return:
        """
        for obs in self.observers:
            obs.update(self)


# 具体的发布者
class StaffNotice(Notice):
    def __init__(self, company_info):
        super().__init__()  # 调用父类对象声明observers属性
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


# 具体的订阅者
class Staff(Observer):
    def __init__(self):
        self.company_info = None

    def update(self, notice):
        self.company_info = notice.company_info


staff_notice = StaffNotice('初始化公司信息')
staff1 = Staff()
staff2 = Staff()
staff_notice.attach(staff1)
staff_notice.attach(staff2)
# print(staff1.company_info) None
# print(staff2.company_info) None
staff_notice.company_info = '假期放假通知！'
print(staff1.company_info)
print(staff2.company_info)
staff_notice.detach(staff2)
staff_notice.company_info = '明天开会！'
print(staff1.company_info)
print(staff2.company_info)
"""
假期放假通知！
假期放假通知！
明天开会！
假期放假通知！
"""
