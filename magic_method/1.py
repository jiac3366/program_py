# 如何赋予对象一些内置类型的属性？
class Company:
    def __init__(self, employ_list):
        self.employ_list = employ_list

    def __getitem__(self, item):
        return self.employ_list[item]

    def __len__(self):
        return len(self.employ_list)

    def __str__(self):
        return ",".join(self.employ_list)

    def __repr__(self):
        return ",".join(self.employ_list)


if __name__ == '__main__':
    # 一些都是对象
    # print(type(int))  # <class 'type'>
    # print(Company.__bases__)  # (<class 'object'>,)
    # print(type(object))  # <class 'type'>
    # print(type(type))  # <class 'type'>
    c = Company(["jj", "xiaoying", "ayuan"])
    # print(type(Company))  # <class 'type'>
    # __str__
    print(c)
    # __repr__
    print(repr(c))
    print(len(c))
    print(c[1])


