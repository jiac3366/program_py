import functools
import random
import time
from functools import wraps


def counter(func):
    value = 0

    @wraps(func)
    def _counter(*args, **kwargs):
        nonlocal value
        value += 1
        return func(*args, **kwargs)

    def print_counter():
        print(f"counter: {value}")

    _counter.print_counter = print_counter
    return _counter


def timer(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        print(f" cost time: {time.time() - t1}")
        return res

    return decorated


@timer
@counter
def random_sleep():
    time.sleep(random.random())


class DelayStart:

    def __int__(self, func, *, duration=1):
        update_wrapper(self, func)
        self.func = func
        self.duration = duration

    def __call__(self, *args, **kwargs):
        print(f"wait {self.duration}")
        time.sleep(self.duration)
        return self.func(*args, **kwargs)


def delay_start(**kwargs):
    return functools.partial(DelayStart, **kwargs)


if __name__ == '__main__':
    random_sleep()
    random_sleep()
    random_sleep.print_counter()
