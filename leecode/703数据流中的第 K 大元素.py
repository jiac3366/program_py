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
        print(self.nums)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        print(self.nums)
        return self.nums[0]


if __name__ == '__main__':
    # kthLargest = KthLargest(3, [4, 5, 8, 2])
    # kthLargest.add(3)
    # kthLargest.add(5)
    # kthLargest.add(10)
    # kthLargest.add(9)
    # kthLargest.add(4)
    print([4, 5, 8, 2][-2])
    print([212,56,6,4, 5, 8, 2][:2])
