import psutil
from task import Task
from safe_queue import SafeQueue
from worker import Worker
import time


class ThreadPool:
    def __init__(self, size=0):
        if not size:
            size = psutil.cpu_count()

        # 任务队列
        self.work_queue = SafeQueue()
        # 线程池
        self.pool = SafeQueue(size)

        for i in range(size):
            self.pool.enqueue(Worker(self.work_queue))

    def start(self):
        for thread in self.pool:
            thread.start()

    def join(self):
        for thread in self.pool:
            thread.stop()
        while self.pool.size():
            thread = self.pool.dequeue()
            thread.join()





    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException()
        self.work_queue.enqueue(item)


class TaskTypeErrorException(Exception):
    pass


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
