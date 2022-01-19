# coding:utf-8

import threading
from threading import Thread

mlocal = threading.local()

# 设置一个成员变量   (主线程、子线程可以分别使用自己局部变量)
mlocal.content = "中国深圳"


# 函数
def work():
    # 修改值
    mlocal.content = "深圳-先行示范区"
    print("变量内容:", mlocal.content)


if __name__ == '__main__':
    thread = Thread(target=work)
    thread.start()
    thread.join()
    print("主线程中内容:", mlocal.content)
