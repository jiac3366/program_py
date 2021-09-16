from create_tree import create_tree
from create_tree import create_tree_by_index
from collections import deque

def pre_order(node):
    """
    前序遍历
    :param node:
    :return:
    """
    if node is None:
        return
    print(node.data)
    pre_order(node.left)
    pre_order(node.right)
    return node


def mid_order(node):
    """
    中序遍历
    :param node:
    :return:
    """
    if node is None:
        return
    mid_order(node.left)
    print(node.data)
    mid_order(node.right)
    return node


def post_order(node):
    """
    后序遍历
    :param node:
    :return:
    """
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.data)
    return node




# 作者：LeetCode - Solution
# class Solution:
#     def preorderTraversal(self, root: TreeNode) -> List[int]:
#         res = list()
#         if not root:
#             return res
#
#         stack = []
#         node = root
#         while stack or node:
#             while node:
#                 res.append(node.val)
#                 stack.append(node)
#                 node = node.left
#             node = stack.pop()
#             node = node.right
#         return res
#
#
#
# class Solution:
#     def inorderTraversal(self, root):
#         res = []
#         stack = []
#         while stack or root:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             res.append(root.val)
#             root = root.right
#         return res
#
#
# class Solution:
#     def postorderTraversal(self, root):
#         if not root:
#             return list()
#
#         res = list()
#         stack = list()
#         prev = None
#
#         while root or stack:
#             while root:
#                 stack.append(root)
#                 root = root.left
#             root = stack.pop()
#             # prev在遍历完右子树之后起作用
#             if not root.right or root.right == prev:
#                 res.append(root.val)
#                 prev = root
#                 root = None
#             else:
#                 stack.append(root)
#                 root = root.right
#
#         return res
#



def N_pre_order(node):
    """二叉树非递归前序遍历---DFS的思想""" """其实和层序遍历有点像--把stack改为queue"""
    if node is None:
        return
    stack = []
    stack.append(node)
    while len(stack) > 0:
        node = stack.pop()
        print(node.data)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

def N_mid_order(node):
    """二叉树非递归中序遍历"""
    if node is None:
        return
    stack = []
    while node is not None or len(stack) > 0:
        # 节点存在的情况
        if node is not None:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.data)
            node = node.right


def N_post_order(node):
    """二叉树非递归后序遍历"""
    if node is None:
        return
    stack_print = []
    stack = []

    while node is not None or len(stack) > 0:  # 后序跟中序很像 只不过记住输出要为了“左右根” -->我们可以用中序的反过来输出达到目的
        if node is not None:
            stack.append(node)
            # 实际上我们的入栈顺序是：根右左
            stack_print.append(node)
            node = node.right
        else:
            node = stack.pop()
            node = node.left
    for i in range(len(stack_print)):
        print(stack_print.pop().data)

def level_order(root):
    """层序遍历"""
    if not root:
        return
    queue = deque()
    queue.append(root)
    while queue:
        root = queue.popleft()
        print(root.data)
        if root.left: queue.append(root.left)
        if root.right: queue.append(root.right)

if __name__ == '__main__':

    # num_list = list(['A', 'B', None, None, 'C', 'D', 'F', None, None, 'G', None, None, 'E', None, None])
    # header = create_tree(num_list)
    num_list = list([3, 9, 20, None, None, 15, 7])
    header = create_tree_by_index(num_list)
    print("前序遍历---------")
    pre_order(header)
    #
    print("中序遍历---------")
    mid_order(header)
    print("后序遍历---------")
    post_order(header)

    # print("非递归前序遍历-------")
    # N_pre_order(header)
    #
    # print("非递归中序遍历-------")
    # N_mid_order(header)

    print("非递归后序遍历-------")
    N_post_order(header)



