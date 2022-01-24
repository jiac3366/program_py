# https://mp.weixin.qq.com/s/B772hZwR9WBZ_6Q9-TemGw
import os
from multiprocessing.dummy import Pool


def get_source(path):
    with open(path, encoding='utf-8') as f:
        count = len(f.readlines())
        print(count)


path_list = ['1', '2', '3']
pool = Pool(10)
pool.map(get_source, path)
