from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        sort_arr = self.mergesort(nums)
        return sort_arr[k - 1]

    def mergesort(self, nums: List[int]):
        if len(nums) == 1:
            return nums

        left = self.mergesort(nums[:len(nums) // 2])
        right = self.mergesort(nums[len(nums) // 2:])
        arr = self.merge_arr(left, right)
        return arr

    def merge_arr(self, arr1, arr2):
        l = 0
        r = 0
        merge_arr = []
        while l <= len(arr1) - 1 and r <= len(arr2) - 1:
            if arr1[l] >= arr2[r]:
                merge_arr.append(arr1[l])
                l += 1
            else:
                merge_arr.append(arr2[r])
                r += 1
        if l != len(arr1):
            merge_arr.extend(arr1[l:])
        if r != len(arr2):
            merge_arr.extend(arr2[r:])
        return merge_arr


if __name__ == '__main__':
    a = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(a)

    # print(Solution().merge_arr([2], [1]))

