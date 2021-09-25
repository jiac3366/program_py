'''
    python线程的事件用于主线程控制其他线程的执行，事件是一个简单的线程同步对象，其主要提供以下的几个方法：
        clear将flag设置为 False
        set将flag设置为 True
        is_set判断是否设置了flag
        wait会一直监听flag，如果没有检测到flag就一直处于阻塞状态
    事件处理的机制：全局定义了一个Flag，当Flag的值为False，那么event.wait()就会阻塞，当flag值为True，
    那么event.wait()便不再阻塞
'''

import time
import threading

event = threading.Event()


def lighter():
    count = 0
    event.set()  # 初始者为绿灯
    while True:
        if 5 < count <= 10:
            event.clear()  # 红灯，清除标志位
            print("\33[41;lmred light is on...\033[0m]")
        elif count > 10:
            event.set()  # 绿灯，设置标志位
            count = 0
        else:
            print('\33[42;lmgreen light is on...\033[0m')

        time.sleep(1)
        count += 1


def car(name):
    while True:
        if event.is_set():  # 判断是否设置了标志位
            print('[%s] running.....' % name)
            time.sleep(1)
        else:
            print('[%s] sees red light,waiting...' % name)
            event.wait()
            print('[%s] green light is on,start going...' % name)


if __name__ == '__main__':
    # startTime = time.time()
    light = threading.Thread(target=lighter, )
    light.start()

    car = threading.Thread(target=car, args=('MINT',))
    car.start()
    endTime = time.time()
    # print('用时：',endTime-startTime)
