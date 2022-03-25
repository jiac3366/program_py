from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager

from queue import Queue

queue = Queue()


class QueueManager(BaseManager): pass


QueueManager.register('get_queue', callable=lambda: queue)
m = QueueManager(address=('', 50000), authkey=b'abracadabra')
s = m.get_server()
s.serve_forever()

