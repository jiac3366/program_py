import time
import threading
from task import Task


class NotTaskInstanceException(Exception):
    pass


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self.queue = queue
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

