from threading import Thread, Lock
import time

lock = Lock()
detail_url = []


# 共享变量不推荐作为线程间通信的方式 除非对锁足够了解 # 而且while会导致一直占用CPU资源
def get_product_detail(detail_url):
    """
    爬取商品详情
    :param detail_url:
    :return:
    """

    while True:
        if len(detail_url):
            print("此时列表url有%d个" % (len(detail_url)))
            detail_url.pop()
            print("get_product_detail start")
            time.sleep(2)
            print("get_product_detail end")


def get_product_url(detail_url):
    """
    爬取商品列表
    :param detail_url:
    :return:
    """
    while True:
        print("get_product_url start")
        time.sleep(4)
        for i in range(20):
            detail_url.append("www.jiac.online/{id}".format(id=i))
        print("get_product_url end")


if __name__ == '__main__':
    start = time.time()
    # 爬取列表线程
    p1 = Thread(target=get_product_url, args=(detail_url,))
    p1.start()
    # p1.join()
    # p2_list = []
    # 爬取详情线程
    for i in range(10):
        p2 = Thread(target=get_product_detail, args=(detail_url,))
        p2.start()
        # p2_list.append(p2)
    # for item in p2_list:
    #     item.join(timeout=2)

    print(time.time() - start)
