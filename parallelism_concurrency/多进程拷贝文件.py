# coding:utf-8

"""
思路分析：
    （1）获取到文件所在目录、文件；
    (2)使用进程拷贝(进程、文件拷贝).
"""
from multiprocessing import Process
import os
import time


def copy(old_file, new_file):
    # 数据源、目标源
    source = open(old_file, "rb")
    target = open(new_file, "wb")
    # 边读边写
    content = source.read()
    target.write(content)
    target.close()
    source.close()


if __name__ == '__main__':
    start = time.time()
    # 目录
    old_folder = "./file"
    new_folder = old_folder + "-copy"
    # 创建目录
    if not os.path.exists(new_folder):
        os.makedirs(new_folder)
    # 拷贝
    lists = os.listdir(old_folder)
    for name in lists:
        # print(name)
        # 拼接目录
        old_folder_name = old_folder + "/" + name
        new_folder_name = new_folder + "/" + name
        # print(old_folder_name)
        # 拷贝
        process = Process(target=copy, args=(old_folder_name, new_folder_name,))
        process.start()
    end = time.time()
    print("计算拷贝花费时间:", (end - start))  # 2.3151447772979736

# from multiprocessing import Pool
# page = [x for x in range(1, MAX_PAGE + 1)]
# # 多进程
# pool = Pool()
# pool.map(main, page)
