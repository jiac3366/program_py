import random


def paopao_sort(list=[]):
    for j in range(len(list) - 1):
        for i in range(len(list) - j - 1):
            if list[i] > list[i + 1]:
                temp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = temp


if __name__ == '__main__':
    list_num = []
    for i in range(10):
        list_num.append(random.randint(1, 10))

    paopao_sort(list_num)
    print(list_num)
