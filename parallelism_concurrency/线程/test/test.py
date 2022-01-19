import threading

num = 0
l = threading.Lock()


def product(name):
    global num

    i = 0
    while i < 1000000:
        i += 1
        num += 1
        # print("第{2}次循环，{0}: set count to {1}".format(name, num, i))


def consume(name):
    global num
    i = 0
    while i < 1000000:
        i += 1
        num -= 1
        # print("第{2}次循环，{0}: set count to {1}".format(name, num, i))


if __name__ == '__main__':
    p1 = threading.Thread(target=consume, args=("consume",))
    p2 = threading.Thread(target=product, args=("product",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    print(num)


