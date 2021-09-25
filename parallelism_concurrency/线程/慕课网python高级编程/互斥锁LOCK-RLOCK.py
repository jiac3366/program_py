from threading import Thread, Lock, RLock  # 可重入的锁
import time

lock = Lock()
number = 0


# 存在线程安全 要加锁-->影响性能
def work():
    global number
    global lock
    # for i in range(100):
    # lock.acquire()
    number += 10
    # lock.release()
    print('thread1:' + str(number) + '\n')
    # time.sleep(0.01)

# GIL  1   1
#          2   2
def work2():
    global number
    global lock
    # for i in range(100):
    # lock.acquire()
    number += 10
    # lock.release()
    print('thread2:' + str(number) + '\n')
    # time.sleep(0.01)


if __name__ == '__main__':
    # start = time.time()
    p1 = Thread(target=work)
    p2 = Thread(target=work2)
    p1.start()
    p2.start()
    # p1.join()
    # p2.join()
    print(number)
    # print(time.time() - start)

#
# 出现死锁的场景：
# 1 连续调用2次acquire() -->RLOCK可以解决 但记住acquire()和release()数量要相等
# -->RLOCK使用场景：同一线程中调用的函数有多次acquire()
# 2 A和B acquire(a) 和 acquire(b)的顺序调转
