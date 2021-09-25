# coding:utf-8
from threading import Thread
import random
import queue
import time

# 队列
mqueue = queue.Queue()


class Productor(Thread):  # 生产者
    def run(self):
        while True:
            number = random.randint(0, 10)
            # 存入队列中
            mqueue.put(number)
            print("生产者生产了数据:", number)
            time.sleep(1)


class Consumer(Thread):
    def run(self):
        while True:
            number = mqueue.get()
            print("消费者消费了----------->", number)


if __name__ == '__main__':
    productor = Productor()
    consumer = Consumer()
    productor.start()
    consumer.start()
