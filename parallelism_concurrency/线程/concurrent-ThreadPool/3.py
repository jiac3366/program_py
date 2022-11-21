from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from concurrent.futures import ProcessPoolExecutor
import time


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


if __name__ == '__main__':

    print("========================")
    start = time.time()
    for num in range(30, 40):
        data = fib(num)
        print("result is {}".format(data))
    print("time:", time.time() - start)
