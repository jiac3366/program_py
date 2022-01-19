import random
import sys
import time




def merge_sort_new(a, p, r):
    if p >= r:
        return






if __name__ == '__main__':
    sys.setrecursionlimit(150000)
    list_num = []
    for i in range(10):
        list_num.append(random.randint(1, 100))

    begin = time.time()
    print(merge_sort_new(list_num))
    end = time.time()
    print(end - begin)