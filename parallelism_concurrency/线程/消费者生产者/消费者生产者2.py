# coding:utf-8

from threading import Thread
import time
import threading

# 商品-手机
phone = None
condition = threading.Condition()


# 生产
def produce():
    global phone
    with condition:
        while True:
            if phone is None:
                print("生产者正在生产产品!")
                phone = "iPhone X"
                # 通知消费者商品已生产完毕,可以来消费了
                condition.notify()
            # 等待消费者消费完毕的通知
            condition.wait()
            time.sleep(2)


# 消费
def consume():
    global phone
    with condition:
        while True:
            if phone is not None:
                print("消费者正在购买商品-->%s" % phone)
                # 消费完毕,将商品设置为None
                phone = None
                # 通知生产者商品已消费完毕,可以继续生产了
                condition.notify()
            # 等待生产者生产完毕的通知
            condition.wait()
            time.sleep(2)


if __name__ == '__main__':
    producer = Thread(target=produce)
    producer.start()
    consumer = Thread(target=consume)
    consumer.start()
