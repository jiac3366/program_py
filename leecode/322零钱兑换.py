class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        lens = amount + 1
        dp = [float("inf") for i in range(lens)]
        dp[0] = 0
        print(dp)
        for i in range(1, lens):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i - coins[j]] + 1)
        return -1 if dp[amount] > amount else dp[amount]


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
