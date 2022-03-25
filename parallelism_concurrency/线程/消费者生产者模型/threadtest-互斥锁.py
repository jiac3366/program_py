# coding:utf-8
from threading import Thread
from threading import Lock
import time

# from threading import

# 1000张票
tickets = 100000
lock = Lock()




# while tickets > 0 没有加锁保护，假如得到锁后不加if tickets > 0: 则会发生超卖
def sale2(number):
    global tickets
    while tickets > 0:
        with lock:
            if tickets > 0:
                tickets -= 1
                print("第00%d窗口正在出售第%d张票..." % (number, tickets))


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
