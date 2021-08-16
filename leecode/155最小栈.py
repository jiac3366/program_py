class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 错误写法： 这里的是if else 逻辑 不是if 就 还  逻辑
        # if len(self.stack) == 0:
        #     self.stack.append((x, x))
        # self.stack.append((x, min(x, self.stack[-1][1])))
        if len(self.stack) == 0:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][1])))

    def pop(self):
        """
        :rtype: None
        """

        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """

        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """

        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()