# coding:utf-8
from threading import Thread
import time

# 1000张票
tickets = 100000


def sale(index):
    global tickets
    while tickets > 0:
        print("第00%d窗口正在出售第%d张票..." % (index, tickets))
        # time.sleep(0.05)
        tickets -= 1


if __name__ == '__main__':
    start = time.time()
    L = []
    for index in range(1, 3):
        thread = Thread(target=sale, args=(index,))
        thread.start()
        L.append(thread)
    for i in L:
        i.join()
    print(time.time() - start)
