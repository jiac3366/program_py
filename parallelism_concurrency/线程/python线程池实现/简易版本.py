import time, threading, Queue
import requests


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self._queue = queue

    def run(self):
        while True:
            _content = self._queue.get()
            print(_content)
            if isinstance(_content, str) and _content == 'quit':
                break
            _res = requests.get(_content)
        print('Bye byes!')


def Producer():
    _urls = ['url1', 'url2', 'url3', 'url4']
    _q = Queue.Queue()
    # 用4个线程同时消费队列
    _workers = build_worker_pool(_q, 4)
    _start_time = time.time()
    for _url in _urls:
        _q.put(_url)
    for _w in _workers:
        _q.put('quit')
    for _w in _workers:
        # join的作用就是为了保证所有的子线程都结束了，再结束父线程
        _w.join()
    _t = time.time() - _start_time
    print(f"Done! Time taken: {_t}")


def build_worker_pool(queue, size):
    _workers = []
    for _ in range(size):
        _worker = Consumer(queue)
        _worker.start()
        _workers.append(_worker)
    return _workers


if __name__ == '__main__':
    Producer()
