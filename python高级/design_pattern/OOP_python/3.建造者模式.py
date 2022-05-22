# coding=utf-8
# coding: utf-8

from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preparation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme_fraiche')
PizzaTopping = Enum('PizzaTopping', 'mozzarella double_mozzarella bacon ham mushrooms red_onion oregano')
STEP_DELAY = 3  # 考虑是示例，单位为秒


class Pizza:

    def __init__(self, name):
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print('preparing the {} dough of your {}...'.format(self.dough.name, self))
        time.sleep(STEP_DELAY)
        print('done with the {} dough'.format(self.dough.name))


class MargaritaBuilder:

    def __init__(self):
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5  # 考虑是示例，单位为秒

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self):
        print('adding the tomato sauce to your margarita...')
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print('done with the tomato sauce')

    def add_topping(self):
        print('adding the topping (double mozzarella, oregano) to your margarita')
        self.pizza.topping.append([i for i in
                                   (PizzaTopping.double_mozzarella, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (double mozzarrella, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your margarita for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your margarita is ready')


class CreamyBaconBuilder:

    def __init__(self):
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 7  # 考虑是示例，单位为秒

    def prepare_dough(self):
        self.progress = PizzaProgress.preparation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self):
        print('adding the crème fraîche sauce to your creamy bacon')
        self.pizza.sauce = PizzaSauce.creme_fraiche
        time.sleep(STEP_DELAY)
        print('done with the crème fraîche sauce')

    def add_topping(self):
        print('adding the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano) to your creamy bacon')
        self.pizza.topping.append([t for t in
                                   (PizzaTopping.mozzarella, PizzaTopping.bacon,
                                    PizzaTopping.ham, PizzaTopping.mushrooms,
                                    PizzaTopping.red_onion, PizzaTopping.oregano)])
        time.sleep(STEP_DELAY)
        print('done with the topping (mozzarella, bacon, ham, mushrooms, red onion, oregano)')

    def bake(self):
        self.progress = PizzaProgress.baking
        print('baking your creamy bacon for {} seconds'.format(self.baking_time))
        time.sleep(self.baking_time)
        self.progress = PizzaProgress.ready
        print('your creamy bacon is ready')


class Waiter:

    def __init__(self):
        self.builder = None
        # 实例属性最好写在__init__里面，哪怕属性不是在初始化时候绑定或者建立，也有写个None
        # 声明一下属性，否则直接在普通方法生成一个实例属性，不符合pycharm的pep8。

    def construct_pizza(self, builder):
        self.builder = builder
        # 按照一定顺序建造
        [step() for step in (builder.prepare_dough,
                             builder.add_sauce, builder.add_topping, builder.bake)]

    # 如果没有property 就要显示地把self.pizza = self.builder.pizza
    @property
    def pizza(self):
        return self.builder.pizza


def validate_style(builders):
    try:
        pizza_style = input('What pizza would you like, [m]argarita or [c]reamy bacon? ')
        builder = builders[pizza_style]()
        valid_input = True
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


def main():
    # 具体建造者（抽象建造者(抽象类)由于python特性已经省略）
    # 但这些建造者除了给对象属性赋值以外，还可以在给builder对象的属性全部赋值之后做依赖关系校验、约束条件校验(46.建造者模式.java)
    builders = dict(m=MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print()
    # 指挥者
    waiter = Waiter()
    waiter.construct_pizza(builder)
    # 最终产品
    pizza = waiter.pizza
    print()
    print('Enjoy your {}!'.format(pizza))


if __name__ == '__main__':
    main()

# =============================================================


from abc import ABCMeta, abstractmethod


# ------产品------
class Player:
    def __init__(self, face=None, body=None, arms=None, legs=None):
        self.face = face
        self.body = body
        self.arms = arms
        self.legs = legs

    def __str__(self):
        return '%s,%s,%s,%s' % (self.face, self.body, self.arms, self.legs)


# ------抽象建造者------
class PlayerBuilder(metaclass=ABCMeta):
    @abstractmethod
    def build_face(self):
        pass

    @abstractmethod
    def build_body(self):
        pass

    @abstractmethod
    def build_arms(self):
        pass

    @abstractmethod
    def build_legs(self):
        pass


# ------具体建造者,隐藏了一个产品的内部结构------
class GirlBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '漂亮的脸蛋'

    def build_body(self):
        self.player.body = '苗条的身材'

    def build_arms(self):
        self.player.arms = '细细的胳膊'

    def build_legs(self):
        self.player.legs = '大长腿'


# ------具体建造者，表示代码------
class MonsterBuilder(PlayerBuilder):
    def __init__(self):
        self.player = Player()

    def build_face(self):
        self.player.face = '绿脸'

    def build_body(self):
        self.player.body = '魁梧的身体'

    def build_arms(self):
        self.player.arms = '粗壮的胳膊'

    def build_legs(self):
        self.player.legs = '粗壮的大腿'


# ------指挥者，构造代码(构造代码和表示代码分开)，可以对构造过程进行更加精细地控制------
class PlayerDirectory():
    def builder_player(self, builder):
        """
        隐藏了装配过程
        :param builder:
        :return:
        """
        builder.build_face()
        builder.build_body()
        builder.build_arms()
        builder.build_legs()
        return builder.player


# ------客户端------
builder = GirlBuilder()
director = PlayerDirectory()
p = director.builder_player(builder)
print(p)  # 漂亮的脸蛋,苗条的身材,细细的胳膊,大长腿
