# coding:utf-8
from threading import Thread
from threading import Lock
import time
# from threading import

# 1000张票
tickets = 100
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
            time.sleep(0.05)
            # 释放锁
            lock.release()


if __name__ == '__main__':
    for index in range(1, 11):
        thread = Thread(target=sale, args=(index,))
        # 启动
        thread.start()
