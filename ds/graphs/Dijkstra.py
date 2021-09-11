# 算法图解7.5
import time

# 创建图 （定死了 不会变）
graph = {
    'start': {
        'a': 6,
        'b': 3
    },
    'a': {'end': 1},
    'b': {
        'a': 3,
        'end': 5,
    },
    'end': {}
}

# 存储每个节点的开销 （会被一直更新） -->从起点出发前往该节点需要的开销
costs = {
    'a': 6,
    'b': 2,
    'end': float('inf')
}

# 存储每个节点的父节点 （会被一直更新）
parents = {
    'a': 'start',
    'b': 'start',
    'end': None
}

# 存储已经处理过的节点
processed = []


# 找出目前开销的散列表中开销最低的节点（从当前节点最近可以到达的点）
def find_lowest_node(costs_dict):
    # 先入为主
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs_dict:
        cost = costs_dict[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


if __name__ == '__main__':
    # find_lowest_node找到目前开销最小的节点（说明这个目前开销最小的节点会在循环中变化）
    # 遍历这个最小的点的邻居--> list类型 ：
    # ----计算从新路径的开销（起点-->目前开销最小的节点-->它的邻居的cost）与旧路径的开销（起点-->它的邻居的cost） 它：目前开销最小的节点
    # ----如果新路径开销更小 更新costs (更新的它的邻居的cost) 和 parent(更新的它的邻居的父节点为它)
    # 更新了它的邻居的相关数据后 -->将它设置为已经处理过

    # 再运行find_lowest_node...以此重复循环直到结束

    start = time.time()
    min_cost_nide = find_lowest_node(costs)
    # 找这个最小开销节点一定程度是为了找通过此点去下一个节点有没有一个更小的路径
    while min_cost_nide is not None:
        cost = costs[min_cost_nide]
        neighbor = graph[min_cost_nide]  # -->dict类型
        for n in neighbor.keys():
            # print(n)
            new_cost = cost + neighbor[n]
            if new_cost < costs[n]:
                # 更新costs
                costs[n] = new_cost
                # 更新parents
                parents[n] = min_cost_nide
        processed.append(min_cost_nide)
        min_cost_nide = find_lowest_node(costs)

    end = time.time()
    print(costs)
    print(parents)
    print(end-start)
