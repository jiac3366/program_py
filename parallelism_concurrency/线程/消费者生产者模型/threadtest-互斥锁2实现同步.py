# coding:utf-8
from threading import Thread
import time
from threading import Lock






def sale2(number):
    global tickets
    global flag
    while flag:
        # 当票数大于0时,售票
        with lock:
            if tickets > 0:
                # print("第00%d窗口正在出售第%d张票..." % (number, tickets))
                # time.sleep(0.01)
                tickets -= 1
            else:
                # print("第00%d窗口车票已销售完毕,谢谢." % number)
                flag = False


if __name__ == '__main__':
    # 票
    tickets = 1000000
    # 先入为主  --默认一直销售火车票
    flag = True
    lock = Lock()
    threads = []
    for index in range(1, 11):
        thread = Thread(target=sale2, args=(index,))
        thread.start()
        threads.append(thread)
    for t in threads:
        t.join()
    print(tickets)
