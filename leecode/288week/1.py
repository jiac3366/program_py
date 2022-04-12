class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """

        num = [int(n) for n in str(num)]
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if num[j] % 2 == 0 and num[i] % 2 == 0 and num[j] > num[i]:
                    num[i], num[j] = num[j], num[i]
                if num[j] % 2 != 0 and num[i] % 2 != 0 and num[j] > num[i]:
                    num[i], num[j] = num[j], num[i]
        num = [str(s) for s in num]
        return int("".join(num))





if __name__ == '__main__':
    o = Solution()
    print(o.largestInteger(65875))


