class Solution:
    def threeSum(self, nums):  # 1158ms
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0: break  # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]: continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]: i += 1
                    while i < j and nums[j] == nums[j + 1]: j -= 1
        return res

    def Python2(self, nums):  # 424ms
        res = []
        nums.sort()
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            else:
                i, j = k + 1, len(nums) - 1
                while i < j:
                    s = nums[i] + nums[j] + nums[k]
                    if s < 0:
                        i += 1
                    if s > 0:
                        j -= 1
                    if s == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
                        # 要记得 思维要严谨
                        # 可能会存在不符合的情况因此陷入死循环
                        i += 1
                        j -= 1
        return res

    def Error_threeSum(self, nums):
        res = []
        nums.sort()
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            else:
                i, j = k + 1, len(nums) - 1
                while i < j:
                    s = nums[i] + nums[j] + nums[k]
                    if s < 0:
                        # 我不太懂这里为什么错误
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                    if s > 0:
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
                    if s == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
        return res

    def geek(self, nums):
        # 遍历排序后数组：
        # 若 nums[i]>0nums[i]>0：因为已经排序好，所以后面不可能有三个数加和等于 00，直接返回结果。
        # 对于重复元素：跳过，避免出现重复解
        # 令左指针 L=i+1L=i+1，右指针 R=n-1R=n−1，当 L<RL<R 时，执行循环：
        # 当 nums[i]+nums[L]+nums[R]==0nums[i]+nums[L]+nums[R]==0，执行循环，判断左界和右界是否和下一位置重复，去除重复解。并同时将 L,RL,R 移到下一位置，寻找新的解
        # 若和大于 00，说明 nums[R]nums[R] 太大，RR 左移
        # 若和小于 00，说明 nums[L]nums[L] 太小，LL 右移
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                # 说明结果不够大 要左下标右移
                if 0 > s:
                    left += 1
                # 说明结果不够小 要右下标左移
                elif 0 < s:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


if __name__ == '__main__':
    m = Solution()
    print(m.geek([-1, 0, 1, 2, -1, -4]))
    import math
    print(math.sqrt(5))




