# coding=utf-8

class Company:
    def __init__(self):
        self.empolyee = ['a', 'b', 'c', 'd']
        self.dicts = {"name": "Chase", "age": 18}

    def __len__(self):
        return len(self.empolyee)

    def __iter__(self):
        index = 0
        while index < len(self.empolyee):
            yield self.empolyee[index]
            index += 2

    def __getitem__(self, item):
        return self.empolyee[item]

    def __str__(self):
        return ".".join(self.empolyee)

    def __repr__(self):
        return ",".join(self.empolyee)

    def __getattr__(self, item):
        return self.dicts[item]

    # 最好没事别重写它
    # def __getattribute__(self, item):
    #     return "jiac"



if __name__ == '__main__':

    obj = Company()

    # 当我需要迭代时 加上__iter__, 对于for来说 obj是generator
    for i in obj:
        print(i)

    # 当我需要下标访问或者切片功能时 加上__getitem__,
    # 实现了__getitem__顺带也实现了__iter__, 如果实现了__iter__优先走它的逻辑
    print(obj[1])
    print(obj[1:])

    print(obj.name)
