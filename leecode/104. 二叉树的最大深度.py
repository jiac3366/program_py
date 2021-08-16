import collections
from tree import create_tree


class Solution(object):
    def maxDepth(self, root):
        """
        104. 二叉树的最大深度
        :type root: TreeNode
        :rtype: int
        """
        res = []
        if not root:
            return []
        queue = collections.deque()
        queue.append(root)
        while queue:
            temp = []
            for i in range(len(queue)):
                node = queue.popleft()
                temp.append(node.data)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(temp)

        return res
        # return len(res)


if __name__ == '__main__':
    s = Solution()
    root = create_tree.create_tree_by_index([3, 9, 20, None, None, 15, 7])
    print(s.maxDepth(root))
