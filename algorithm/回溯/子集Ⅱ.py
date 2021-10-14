# -*- coding: utf-8 -*-
class Solution:
    def subsetsWithDup(self, nums):
        self.res = []

        # eg: [1, 3, 3]
        # uniqe: [1, 3]
        # count: [1, 2]
        from collections import Counter
        countMap = Counter(nums)  # {3:1, 1:1}
        # 假设遍历map是无序的
        k = 0
        uniqeNum = []
        count = []
        for item in nums:
            if item in countMap:
                uniqeNum.append(item)
                count.append(countMap[item])
                countMap.pop(item)
        print(uniqeNum)
        print(count)


        def backtrace(count, uniqeNum, k, path):
            if k == len(uniqeNum):
                self.res.append(path[:])
                return

            # 先遍历count数组 获取当前层可供选择的方案数 如果count[k]=2, 则方案有放0、1、2个
            # 他吗的 这里记得 + 1
            for c in range(count[k] + 1):
                # 放0、1、2个由第2个循环负责
                for i in range(c):
                    path.append(uniqeNum[k])
                backtrace(count, uniqeNum, k + 1, path)
                for i in range(c):
                    path.pop()

        backtrace(count, uniqeNum, 0, [])
        return self.res


if __name__ == '__main__':
    c = Solution()
    print(c.subsetsWithDup([1, 3, 3]))
