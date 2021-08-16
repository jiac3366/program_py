from collections import deque


class Solution:

    # 堆排序求出最大值 但不知道如何去除最先加入的元素
    def maxSlidingWindow2(self, nums, k):
        import heapq
        heap_list = [nums[i] for i in range(k)]
        heapq.heapify(heap_list)
        res = []
        res.append(heapq.nlargest(1, heap_list)[0])
        for i in range(k, len(nums)):
            # heap_list = heap_list[1:]
            heapq.heappush(heap_list, nums[i])
            res.append(heapq.nlargest(1, heap_list)[0])
        print(res)

    def maxSlidingWindow(self, nums, k):
        if not nums:
            return []
        res = []
        # 存放的是数的下标
        wins = deque()
        # wins = []
        for i, item in enumerate(nums):
            # 窗口左边的值已经不得不要扔掉: wins[0] <= i - k表示已经左边出界
            if i >= k and wins[0] <= i - k:
                go = wins.popleft()
                print("%d超过边界，走了" % nums[go])
            while wins and nums[wins[-1]] <= item:
                # 因为要赶走的是比较小的下标的数(最新加进来的下标在wins右边) 所以用pop()
                s = wins.pop()
                print("%d被赶走，被%d赶走" % (nums[s], nums[i]))
            # nums[wins[-1]] > item 照样把i加进wins
            wins.append(i)
            print("%d被加入" % nums[i])
            print("滑动窗口:", wins)
            # tips: 以变化的i作为一些判断的方向：判断到底什么时候可以把窗口的最大值加入我的res里：i >= k - 1的时候
            if i >= k - 1:
                res.append(nums[wins[0]])
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, 1, 2, 0, 5], 3))  # 预期[3,3,2,5]
