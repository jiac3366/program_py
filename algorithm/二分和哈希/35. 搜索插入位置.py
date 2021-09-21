# -*- coding: utf-8 -*-
def searchInsert(nums, target) -> int:
    if not nums: return 0
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            if mid == 0 or nums[mid - 1] < target:
                return mid
            else:
                right = mid - 1
    return 0 if target < nums[0] else 1


if __name__ == '__main__':
    print(searchInsert([1, 3, 5, 6], 7))
