import uuid
import time
from worker_pool import ThreadPool


class Task:
    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.args = args
        self.kwargs = kwargs
        self.id = uuid.uuid4()

    def __str__(self):
        return ",".join(list(self.args)) + " task id is " + str(self.id)


# def test_func(name):
#     print(name + "test")
#     time.sleep(2)
#
#
# if __name__ == '__main__':
#     t1 = Task(test_func, "jiac", "kk")
#     print(t1)


def process():
    time.sleep(1)
    print('This is a SimpleTask callable function 1.')


if __name__ == '__main__':
    pool = ThreadPool(5)
    pool.start()
    for i in range(20):
        simple_task = Task(process)
        pool.put(simple_task)
    pool.join()
    print('任务处理结束')
