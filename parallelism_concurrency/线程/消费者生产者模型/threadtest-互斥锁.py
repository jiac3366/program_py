# coding:utf-8
from threading import Thread
from threading import Lock
import time

# from threading import

# 1000张票
tickets = 100000
lock = Lock()


def sale(number):
    global tickets
    # 线程冲突 导致有可能2个线程同时判断ticket>0-->说明这个全局变量的变化对于线程是有延迟的
    while tickets > 0:
        # 线程若等待后获得锁 说明进入临界区 再判断这个全局变量的值
        if lock.acquire():
            # 当小于等于0,跳出循环
            if tickets <= 0:  # 释放
                # 释放锁
                lock.release()
                break
            print("第00%d窗口正在出售第%d张票..." % (number, tickets))
            tickets -= 1
            # time.sleep(0.05)
            # 释放锁
            lock.release()

# while tickets > 0 没有加锁保护，假如得到锁后不加if tickets > 0: 则会发生超卖
def sale2(number):
    global tickets
    while tickets > 0:
        with lock:
            if tickets > 0:
                tickets -= 1
                # print("第00%d窗口正在出售第%d张票..." % (number, tickets))


if __name__ == '__main__':
    threads = []
    for index in range(1, 11):
        thread = Thread(target=sale2, args=(index,))
        threads.append(thread)
        # 启动
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(tickets)
