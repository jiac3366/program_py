class Animal():
    def __init__(self):
        self.name = "动物园"
        self.weight = 0

    def jump(self):
        print("jump")




# 用 __call__() 弥补 hasattr() 函数的短板, 就可以判断该指定的名称，到底是类属性还是类方法
if __name__ == '__main__':
    animal = Animal()
    if hasattr(animal.name, "__call__"):
        print(1)  # 不输出
    if hasattr(animal.jump, "__call__"):
        print(2)  # 输出
