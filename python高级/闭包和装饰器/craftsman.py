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


if __name__ == '__main__':
    random_sleep()
    random_sleep()
    random_sleep.print_counter()
