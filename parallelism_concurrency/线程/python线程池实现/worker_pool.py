import psutil


from safe_queue import SafeQueue
import threading
from main import Task


class NotTaskInstanceException(Exception):
    pass


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue = queue  # 任务队列
        self.stop_event = threading.Event()

    def run(self) -> None:
        while True:
            # 变量默认为False 当为True时 说明线程被通知停止
            # 注意 不能直接这样判断：if self.stop_event，而是要判断event里面的flag
            if self.stop_event.is_set():
                break
            task = self.queue.dequeue()
            if not isinstance(task, Task):
                raise NotTaskInstanceException
            # 为什么要加* **
            task.callable(*task.args, **task.kwargs)

    def stop(self):
        self.stop_event.set()


class ThreadPool:
    def __init__(self, size=0):
        if not size:
            size = psutil.cpu_count()

        # 任务队列
        self.work_queue = SafeQueue()
        # 线程池
        self.pool = SafeQueue(size)

        for i in range(size):
            worker = Worker(self.work_queue)
            self.pool.enqueue(worker)

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


