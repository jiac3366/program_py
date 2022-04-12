# coding=utf-8
class Solution(object):
    def maximumProduct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.max = 0
        # nums = [int(n) for n in str(nums)]
        self.backtrack(nums, 0, k)
        return self.max

    def backtrack(self, nums, level, k):
        if level == k:
            maxNum = 1
            for n in nums:
                maxNum *= n
            self.max = max(maxNum, self.max)
            return

        for i in range(len(nums)):
            nums[i] += 1
            self.backtrack(nums, level + 1, k)
            nums[i] -= 1





if __name__ == '__main__':
    o = Solution()
    print(o.maximumProduct([6,3,3,2],2))
