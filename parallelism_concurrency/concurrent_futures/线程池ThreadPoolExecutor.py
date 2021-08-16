from concurrent.futures import ThreadPoolExecutor, as_completed, wait
from concurrent.futures import ProcessPoolExecutor
import time


# future对象的方法：
# 可以获取线程的执行结果result()、是否完成的状态done()
# 也可以控制线程中途退出cancel()

# 如何在主线程获取批量线程的运行状态？
# 1 作者更加偏向：通过as_completed(futures对象列表)返回可迭代对象 每个元素就是已完成的线程(future对象) 并用result()查看哪些已完成
# 2 更加简便：使用ThreadPoolExecutor实例的map()方法 返回可迭代对象 每个元素就是已完成的线程(future对象)的result()返回值
# 1方法谁先完成处理谁 但2方法输出顺序与任务列表的顺序一致 更底层的multiprocessing库也有类似的imap() imap_inorder()方法

# wait作用是阻塞主线程 等待某些事件的发生 再往下执行

def fib(n):
    if n <= 2:
        return 1
    return fib(n - 2) + fib(n - 1)


def io_sleep(num):
    time.sleep(num)
    return num


if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        # all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
        all_task = [executor.submit(io_sleep, (num)) for num in [2] * 30]
        start = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("result is {}".format(data))
        print("time:", time.time() - start)
