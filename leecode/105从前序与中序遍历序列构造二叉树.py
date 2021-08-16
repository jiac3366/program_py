"""输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。"""


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return
        # write code here
        root = pre.pop(0)
        index_mid = tin.index(root.val)
        root.left = self.reConstructBinaryTree(pre, tin[:index_mid])
        root.right = self.reConstructBinaryTree(pre, tin[index_mid:])
        return root


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    mid = [4, 7, 2]
    print(mid[:mid.index(2)])
    print(mid[mid.index(2) + 1:])
