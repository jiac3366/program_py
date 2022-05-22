# !/usr/bin/env python
# encoding: utf-8

class Target(object):
    def request(self):
        print
        'Target request'


class Adaptee(object):
    def specialRequest(self):
        print
        'Adaptee specialRequest'


class Adpater(object):
    def __init__(self, adpatee):
        self.adpatee = adpatee

    def request(self):
        self.adpatee.specialRequest()


if __name__ == '__main__':
    objects = []
    a = Target()
    b = Adaptee()

    objects.append(a)
    objects.append(Adpater(b))  # 适配接口

    for obj in objects:
        obj.request()  # 调用相同接口


# ===================================================
# coding=utf-8


class Dog():
    def __init__(self, name):
        self.name = name

    def wangwang(self):
        print
        'my name is' + self.name + '。。。汪汪汪。。。'

    def dog_run(self):
        print
        'dog is running'


class Cat():
    def __init__(self, name):
        self.name = name

    def miaomiao(self):
        print
        'my name is' + self.name + '。。。喵喵喵。。。'

    def cat_run(self):
        print
        'cat is running'


class Sheep():
    def __init__(self, name):
        self.name = name

    def miemie(self):
        print
        'my name is' + self.name + '。。。咩咩。。。'

    def sheet_run(self):
        print
        'sheet is running'


class Adapter():
    def __init__(self, animal, adapted_methods):
        '''
        :type adapted_methods: dict
        '''
        self.__dict__.update(adapted_methods)


def main():
    animals = [Dog('旺财')]
    cat = Cat('大脸猫')
    sheep = Sheep('喜洋洋')

    animals.append(Adapter(cat, {'wangwang': cat.miaomiao, 'dog_run': cat.cat_run}))
    animals.append(Adapter(sheep, {'wangwang': sheep.miemie, 'dog_run': sheep.sheet_run}))

    for a in animals:
        a.wangwang()
        a.dog_run()
        print
        ''


def main2():
    animals = []
    dog = Dog('旺财')
    cat = Cat('大脸猫')
    sheep = Sheep('喜洋洋')
    animals.append(Adapter(cat, {'speak': dog.wangwang, 'run': dog.dog_run}))
    animals.append(Adapter(cat, {'speak': cat.miaomiao, 'run': cat.cat_run}))
    animals.append(Adapter(sheep, {'speak': sheep.miemie, 'run': sheep.sheet_run}))

    for a in animals:
        a.speak()
        a.run()
        print
        ''


if __name__ == "__main__":
    main()
    print
    '* ' * 20
    main2()

# =====================================


