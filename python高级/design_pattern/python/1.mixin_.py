class Person():
    def __init__(self, name):
        self.name = name

    def walk(self):
        print('行走')


class StudyMixin():
    # Mixin类防止多个类要添加相同的功能，就去每个类写几个方法，多少个类复制黏贴多少次，重复较多，要修改的时候又要去每个类去修改
    # 类似一个插件，mixin类的方法可以直接访问基本类的方法和属性
    def study(self):
        print(self.name + '...在上课...')


class Student(Person, StudyMixin):
    def __init__(self, name, age):
        Person.__init__(self, name)
        self.age = age

    def eat(self):
        print(self.name + '...在吃饭...')


Student('小明', 10).study()
# StudyMixin().study()
