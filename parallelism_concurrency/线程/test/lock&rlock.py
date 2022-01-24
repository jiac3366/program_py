import threading

num = 0
lock = threading.Lock()


def consume(name):
    global num
    i = 0
    while i < 10000000:
        # with l:
        i += 1
        num -= 1
        # print("第{2}次循环，{0}: set count to {1}".format(name, num, i))


def product(lock):
    global num
    if num == 50: return
    i = 0
    # while i < 1000000:
    lock.acquire()
    i += 1
    num += 1
    lock.release()
    product(lock)
    # lock.release()


if __name__ == '__main__':
    lock = threading.Lock()
    # p1 = threading.Thread(target=consume, args=("product",))
    p2 = threading.Thread(target=product, args=(lock,))
    p2.start()
    p2.join()
    print(num)
