import threading


class SafeQueue:
    """2022.1.24新东西：
    1、如果为了方便弄2个信号量not_full和not_empty，前提是他们都得传入同一个lock
    2、实现了__getitem__，对象即可通过下标和for遍历
    """

    def __init__(self, capacity: int = 0):
        self.lock = threading.RLock()
        self.capacity = capacity
        self.queue = []
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)

    # def __iter__(self):
    #     return QueueItorator(self.queue)

    def __getitem__(self, item):
        return self.queue[item]

    def enqueue(self, element):
        with self.not_full:
            if self.capacity:
                while self.size() >= self.capacity:
                    self.not_full.wait()
            self.queue.append(element)
            self.not_empty.notify()

    def dequeue(self):
        with self.not_empty:
            if self.capacity == 0:
                while self.size() <= 0:
                    self.not_empty.wait()
            item = self.queue.pop(0)
            self.not_full.notify()
        return item

    def size(self):
        # with self.lock:
        n = len(self.queue)
        return n


class QueueItorator:
    def __init__(self, queue):
        self.queue = queue
        self.index = 0

    def __next__(self):
        try:
            item = self.queue[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return item

    def __iter__(self):
        return self


if __name__ == '__main__':
    queue = SafeQueue(100)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    # __getitem__
    for i in range(queue.size()):
        print(queue[i])

    for i in queue:
        print(i)

    # q = iter(queue)
    # print(q)

    # def product():
    #     while True:
    #         queue.enqueue(1)
    #         print('enqueue')
    #         time.sleep(3)
    #
    #
    # def consumer():
    #     while True:
    #         item = queue.dequeue()
    #         print('dequeue %d' % item)
    #         time.sleep(3)
    #
    #
    # t1 = threading.Thread(target=product)
    # t2 = threading.Thread(target=consumer)
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
