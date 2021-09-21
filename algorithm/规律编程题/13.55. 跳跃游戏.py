# -*- coding: utf-8 -*-
def canJump(nums):
    distance = len(nums) - 1
    i = 0
    max_distance = 0
    while i < len(nums):
        if i < max_distance and i + nums[i] > max_distance:
            max_distance = i + nums[i]
        i += 1
    return max_distance >= distance

if __name__ == '__main__':
    canJump([3,2,1,0,4])
