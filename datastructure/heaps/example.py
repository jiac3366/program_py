# -*- coding: utf-8 -*-

import heapq


class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.nums, val)
        # print(self.nums)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        # print(self.nums)
        return self.nums[0]


if __name__ == '__main__':
    nums = [2, 3, 5, 1, 54, 23, 132]
    print(nums[:3])
    heapq.heapify(nums)
    # print(nums)
    print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
    # out: [1, 2, 3, 5, 23, 54, 132]
