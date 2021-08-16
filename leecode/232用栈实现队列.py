"""用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。"""


class Solution:
    def __init__(self):
        self.A = []
        self.B = []

    def push(self, node):
        # write code here

        self.A.append(node)

    def pop(self):
        # return xx
        if self.B:
            return self.B.pop()
        elif not self.A:
            return None
        else:
            while len(self.A) > 0:
                self.B.append(self.A.pop())
            return self.B.pop()

#["MyQueue","push","push","peek","pop","empty"]
# [[],[1],[2],[],[],[]]
class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.right = []
        self.left = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.right.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.left:
            return self.left.pop()
        elif self.right:
            while self.right:
                self.left.append(self.right.pop())
            return self.left.pop()
        else:
            return None

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.left:
            while self.right:
                self.left.append(self.right.pop())
        return self.left[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.left and self.right

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
