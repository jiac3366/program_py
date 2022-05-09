class Singleton:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "fuck"):
            cls.fuck = super(Singleton, cls).__new__(cls)
        return cls.fuck


class Myclass(Singleton):
    def __init__(self, a):
        self.a = a


a = Myclass(10)
b = Myclass(20)  #

print(a.a)
print(b.a)
print(id(a) == id(b))  # True
