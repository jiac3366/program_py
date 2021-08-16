class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def create_tree(num_list):
    """
    构建二叉树-根据层序创建
    :return:
    """
    if not num_list:
        return
    data = num_list.pop(0)
    if data is None:
        return
    # 前序遍历创建
    root = TreeNode(data)
    root.left = create_tree(num_list)
    root.right = create_tree(num_list)
    return root


def create_tree_by_index(num_list):
    def helper(num_list, i):
        """
        构建二叉树-根据下标创建
        :return:
        """
        if i > len(num_list):
            return
        if num_list[i] is None:
            return
        root = TreeNode(num_list[i])
        root.left = helper(num_list, 2 * i + 1)
        root.right = helper(num_list, 2 * i + 2)
        return root

    return helper(num_list, 0)


if __name__ == '__main__':
    create_tree_by_index([3, 9, 20, None, None, 15, 7])
