# coding:utf-8

from threading import Thread
import time
import threading

phone = None
condition = threading.Condition()


# 生产
def produce():
    global phone
    with condition:
        while True:
            if phone is not None:
                print('等待消费者消费')
                time.sleep(3)
                condition.wait()
            phone = 'iphone'
            print("生产者生产了手机")
            time.sleep(3)
            condition.notify()
            print("通知消费者")
            time.sleep(3)


# 消费
def consume():
    global phone

    with condition:
        while True:
            if phone is None:
                print('等待生产者生产')
                time.sleep(3)
                condition.wait()
            phone = None
            print("消费者消费了手机")
            time.sleep(3)
            condition.notify()
            print("通知生产者")
            time.sleep(3)


if __name__ == '__main__':
    producer = Thread(target=produce)
    producer.start()
    consumer = Thread(target=consume)
    consumer.start()
    producer.join()
    consumer.join()
