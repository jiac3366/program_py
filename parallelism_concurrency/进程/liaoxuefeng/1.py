# task_master.py

import random, time, queue
from multiprocessing.managers import BaseManager
from multiprocessing import Process, Queue


# # 发送任务的队列:
# task_queue = queue.Queue()
# # 接收结果的队列:
# result_queue = queue.Queue()


# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass


if __name__ == '__main__':

    task_queue = queue.Queue()
    result_queue = queue.Queue()

    # class Worker(Process):
    #     def __init__(self, q):
    #         self.q = q
    #         super(Worker, self).__init__()
    #
    #     def run(self):
    #         for i in range(10):
    #             n = random.randint(0, 10000)
    #             print('Put task %d...' % n)
    #             self.q.put(n)

    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    QueueManager.register('get_task_queue', callable=lambda: task_queue)
    QueueManager.register('get_result_queue', callable=lambda: result_queue)
    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('127.0.0.1', 50000), authkey=b'abc')
    # 启动Queue:
    # server = manager.get_server()
    # server.serve_forever()

    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 放几个任务进去:
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)
    # 从result队列读取结果:
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=100)
        print('Result: %s' % r)
    # 关闭:
    manager.shutdown()
    print('master exit.')
