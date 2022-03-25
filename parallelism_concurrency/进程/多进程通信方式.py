from multiprocessing import Process, Queue, Pipe
from multiprocessing import Manager
from multiprocessing import Pool

# queue的Queue不适用多进程编程(但是分布式进程是可以的?) 多进程编程可以用multiprocessing中的Queue和Manager()中的Queue
# 但注意：multiprocessing中的Queue不能用于multiprocessing中Pool创建的进程之间的通信
# 其Pool创建的进程之间的通信需要用到Manager()中的Queue
# Pipe只能适用于2个进程的通信 Pipe性能高于Queue

# 进程之间不能共享全局变量(进程之间的数据完全隔离，它会把全局变量的数据全部复制一份，复制到子进程，是相互独立的）

# 通信方式：
# 管道：Pipe()
# 消息队列：进程池：Manager().Queue()；普通进程：multiprocessing的Queue
# 共享内存（信号量）：Manager().dict()...有很多常见的数据结构  用法和线程间的同步一样

