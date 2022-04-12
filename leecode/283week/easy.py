# coding=utf-8


class Solution:
    def minimalKSum(self, nums, k):
        max_num = max(nums)
        bitmap = [0 for _ in range(max_num)]
        for num in nums:
            bitmap[num - 1] = 1
        print(bitmap)
        sum_num = 0
        c = 1
        count = 0
        for i in bitmap:
            if count == k:
                break
            if i == 0:
                sum_num += c
                c += 1
                count += 1
        # ======================
        # n = len(nums) + k
        # i = 1
        # sum_num = 0
        # while len(nums) < n:
        #     if i > len(nums):
        #         sum_num += i
        #         nums.append(i)
        #         i += 1
        #
        #     elif bitmap[i - 1] == 1:
        #         i += 1
        #     else:
        #         nums.append(i)
        #         sum_num += i
        #         i += 1

        return sum_num


if __name__ == '__main__':
    s = Solution()
    print(s.minimalKSum([5, 6], 6))
