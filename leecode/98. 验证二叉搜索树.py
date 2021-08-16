# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        if not root:
            return True
        stack = []
        node = root
        pre = None

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                if pre and pre.val >= node.val:
                    return False
                pre = node
                node = node.right
        return True
