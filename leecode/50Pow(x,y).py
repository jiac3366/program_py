class Solution:
    def myPow(self, x, n):

        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n / 2)

    def Pow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1
        return pow

    def my(self,x,n):
        res = 1
        for i in range(n):
            res *= x
        return res

if __name__ == '__main__':
    s = Solution()
    import time
    s1 = time.time()
    print(s.Pow(5, 50000))
    # print(s.my(5, 50000))
    print(time.time()-s1)

