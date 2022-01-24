import uuid
import time


class Task:
    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.args = args
        self.kwargs = kwargs
        self.id = uuid.uuid4()

    def __str__(self):
        return ",".join(list(self.args)) + " task id is " + str(self.id)


def test_func(name):
    print(name + "test")
    time.sleep(2)


if __name__ == '__main__':
    t1 = Task(test_func, "jiac", "kk")
    print(t1)
