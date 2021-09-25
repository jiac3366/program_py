# coding:utf-8

from threading import Thread
import time
import threading

# 商品-手机
phone = None
condition = threading.Condition()
# 12.Python异步使用场景有那些？
# 异步的使用场景:
#
# 1、 不涉及共享资源，获对共享资源只读，即非互斥操作
#
# 2、 没有时序上的严格关系
#
# 3、 不需要原子操作，或可以通过其他方式控制原子性
#
# 4、 常用于IO操作等耗时操作，因为比较影响客户体验和使用性能
#
# 5、 不影响主线程逻辑

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
