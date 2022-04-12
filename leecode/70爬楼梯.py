class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        # 1 2 3 5 8
        a, b, c = 1, 2, 3
        for i in range(3, n + 1):
            c = a + b
            # 1,2,3,5
            # a b c
            #   a b c
            # a = b 在先 是因为防止b的值被b = c修改
            a = b
            b = c
        return c
    def Fibonacci2(self, n):
        # write code here 更简洁
        a = 1
        b = 2
        for i in range(n-2):
            a, b = b, a + b
            yield b
            print(b)

    #
if __name__ == '__main__':
    s = Solution()
    print([i for i in s.Fibonacci2(5)])
