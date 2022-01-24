from threading import Semaphore


class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.q = []
        self.mutex = Semaphore(1)
        self.full = Semaphore(0)
        self.empty = Semaphore(capacity)

    def enqueue(self, element: int) -> None:
        self.empty.acquire()
        with self.mutex:
            self.q.append(element)
        self.full.release()

    def dequeue(self) -> int:
        self.full.acquire()
        with self.mutex:
            res = self.q.pop(0)
        self.empty.release()
        return res

    def size(self) -> int:
        return len(self.q)


from collections import deque
from threading import Semaphore


class BoundedBlockingQueue2(object):

    def __init__(self, capacity: int):
        self.left_capacity = Semaphore(capacity)
        self.curr_capacity = Semaphore(0)
        self.data = deque([])

    def enqueue(self, element: int) -> None:
        # 空位 -1
        self.left_capacity.acquire()
        # 占位 + 1
        self.curr_capacity.release()
        # 必须在信号量执行之后，进行操作：
        self.data.append(element)

    def dequeue(self) -> int:
        # 空位 + 1
        self.left_capacity.release()
        # 占位 - 1
        self.curr_capacity.acquire()
        # 必须在信号量执行之后，进行操作：
        return self.data.popleft()

    def size(self) -> int:
        return len(self.data)


