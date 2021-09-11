# -*- coding: utf-8 -*-

def isStraight(nums):
    # 除0以外不能重复
    if not nums:
        return False

    dup = [False for _ in range(15)]
    index = 0
    max = -1
    min = 100
    while index < 5:

        if nums[index] != 0:
            if dup[nums[index]]: return False
            else: dup[nums[index]] = True

            if nums[index] > max: max = nums[index]
            if nums[index] < min: min = nums[index]

        index += 1
    return (max - min) <5