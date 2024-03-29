import threading
import time


class RWlock(object):
    def __init__(self):
        self._lock = threading.Lock()
        self._extra = threading.Lock()
        self.read_num = 0

    def read_acquire(self):
        with self._extra:
            self.read_num += 1
            if self.read_num == 1:
                self._lock.acquire()

    def read_release(self):
        with self._extra:
            self.read_num -= 1
            if self.read_num == 0:
                self._lock.release()

    def write_acquire(self):
        self._lock.acquire()

    def write_release(self):
        self._lock.release()


class RWLock(object):
    def __init__(self):
        self.lock = threading.Lock()
        self.rcond = threading.Condition(self.lock)
        self.wcond = threading.Condition(self.lock)
        self.read_waiter = 0  # 等待获取读锁的线程数
        self.write_waiter = 0  # 等待获取写锁的线程数
        self.state = 0  # 正数：表示正在读操作的线程数   负数：表示正在写操作的线程数（最多-1）
        self.owners = []  # 正在操作的线程id集合
        self.write_first = True  # 默认写优先，False表示读优先

    def write_acquire(self, blocking=True):
        # 获取写锁只有当
        me = threading.get_ident()
        with self.lock:
            while not self._write_acquire(me):
                if not blocking:
                    return False
                self.write_waiter += 1
                self.wcond.wait()
                self.write_waiter -= 1
        return True

    def _write_acquire(self, me):
        # 获取写锁只有当锁没人占用，或者当前线程已经占用
        if self.state == 0 or (self.state < 0 and me in self.owners):
            self.state -= 1
            self.owners.append(me)
            return True
        if self.state > 0 and me in self.owners:
            raise RuntimeError('cannot recursively wrlock a rdlocked lock')
        return False

    def read_acquire(self, blocking=True):
        me = threading.get_ident()
        with self.lock:
            while not self._read_acquire(me):
                if not blocking:
                    return False
                self.read_waiter += 1
                self.rcond.wait()
                self.read_waiter -= 1
        return True

    def _read_acquire(self, me):
        if self.state < 0:
            # 如果锁被写锁占用
            return False

        if not self.write_waiter:
            ok = True
        else:
            ok = me in self.owners
        if ok or not self.write_first:
            self.state += 1
            self.owners.append(me)
            return True
        return False

    def unlock(self):
        me = threading.get_ident()
        with self.lock:
            try:
                self.owners.remove(me)
            except ValueError:
                raise RuntimeError('cannot release un-acquired lock')

            if self.state > 0:
                self.state -= 1
            else:
                self.state += 1
            if not self.state:
                if self.write_waiter and self.write_first:  # 如果有写操作在等待（默认写优先）
                    self.wcond.notify()
                elif self.read_waiter:
                    self.rcond.notify_all()
                elif self.write_waiter:
                    self.wcond.notify()

    read_release = unlock
    write_release = unlock


def product(i):
    global num
    global lock
    global mutex

    while num > 0:
        # mutex.acquire()
        lock.read_acquire()
        # 从判断num > 0 到拿到锁有个空隙 有可能已经读进寄存器但是早已经被 别人争到了锁

        if num > 0:
            print(str(i) + "号线程获取读锁")
            num -= 1
            print("剩余次数", num)
        else:
            break
            # time.sleep(1)
        lock.read_release()
        # mutex.release()


import threading
from readerwriterlock import rwlock

WEEKDAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
today = 0
marker = threading.Lock()


def calendar_reader(id_number):
    global today
    name = 'Reader-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        marker.acquire()
        print(name, 'sees that today is', WEEKDAYS[today])
        marker.release()


def calender_writer(id_number):
    global today
    name = 'Write-' + str(id_number)
    while today < len(WEEKDAYS) - 1:
        marker.acquire()
        today = (today + 1) % 7
        print(name, 'updated date to ', WEEKDAYS[today])
        marker.release()


if __name__ == '__main__':
    #  create ten reader threads
    for i in range(10):
        threading.Thread(target=calendar_reader, args=(i,)).start()
    #  ...but only two writer threads
    for i in range(2):
        threading.Thread(target=calender_writer, args=(i,)).start()

# if __name__ == '__main__':
#     num = 1000000
#     lock = RWlock()
#     mutex = threading.Lock()
#     thread_list = []
#     t1 = time.sleep()
#     for i in range(5):
#         p = threading.Thread(target=product, args=(i,))
#         thread_list.append(p)
#     for p in thread_list:
#         p.start()
#     for p in thread_list:
#         p.join()
#
#     print(num)
