# 算法图解6.5 找你朋友圈中最近的芒果销售商 这个图的边没有权重 BFS DFS
from collections import deque

# 创建图
graph = {}
graph['you'] = ['bob', 'claire', 'alice']
graph['bob'] = ['anuj', 'peggy']
graph['anuj'] = []
graph['peggy'] = []
graph['claire'] = ['thon', 'jonnym']
graph['alice'] = ['peggy']
graph['thon'] = []
graph['jonny'] = []


def is_mongo_seller(item):
    return item[-1] == 'm'


def BFS_mongo_seller(graphs):
    # deque用法：
    # appendleft 往左边添加一个元素
    # append 往右边添加一个元素
    # popleft 获取最左边一个元素，并在队列中删除
    # pop 获取最右边一个元素，并在队列中删除
    search_queue = deque()
    search_queue += graphs['you']
    searched = []  # 记录是否被访问过
    while search_queue:
        person = search_queue.popleft()
        # 如果未被访问
        if not person in searched:
            if is_mongo_seller(person):
                print(person + " is a mongo seller! ")
                searched.append(person)
                return True
            else:
                # 记录此节点已被访问
                searched.append(person)
                search_queue += graph[person]
    return False


if __name__ == '__main__':
    print(BFS_mongo_seller(graph))  # --> 返回 False 没有mongo seller

    # BFS用于非加权图中找最短路径
