import random
import datetime
import time

list_num = []
for i in range(10):
    list_num.append(random.randint(1, 100))


# print(list_num)


def find_small(list):
    min = list[0]
    min_index = 0
    for i in range(1, len(list)):
        if list[i] < min:
            min = list[i]
            min_index = i
    return min_index


def chice_sort(list):
    new_arr = []
    for i in range(0, len(list)):
        s = find_small(list)
        new_arr.append(list.pop(s))
    return new_arr


if __name__ == '__main__':
    # begin = datetime.datetime.now()
    begin = time.time()
    print(list_num)
    l = chice_sort(list_num)
    end = time.time()
    print("this is the sorted list:")
    print(l)
    print(end - begin)
    # print("it needs time {}".format(end-begin))
