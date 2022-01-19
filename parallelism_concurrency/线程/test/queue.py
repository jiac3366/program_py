import threading


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.lock = threading.Lock()
        self.capacity = capacity
        self.queue = []
        # self.not_full = threading.Condition(self.lock)
        # self.not_empty = threading.Condition(self.lock)
        self.cond = threading.Condition(self.lock)

    def enqueue(self, element: int) -> None:
        with self.cond:
            while self.size() >= self.capacity:
                self.cond.wait()
            self.queue.append(element)
            self.cond.notify()

    def dequeue(self) -> int:
        with self.cond:
            while self.size() <= 0:
                self.cond.wait()
            item = self.queue.pop(0)
            self.cond.notify()
        return item

    def size(self) -> int:
        n = len(self.queue)
        return n
