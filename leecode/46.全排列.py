from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        used = [0 for _ in range(len(nums))]
        self.helper(nums, result, 0, used, [])
        return result

    def helper(self, nums, res, level, used, path):
        if level == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i] == 1:
                continue
            path.append(nums[i])
            used[i] = 1
            self.helper(nums, res, level + 1, used, path)
            path.pop()
            used[i] = 0
        return


if __name__ == "__main__":
    print(Solution().permute([1, 3, 2]))
    # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
    # [[1, 3, 2], [1, 2, 3], [3, 1, 2], [3, 2, 1], [2, 1, 3], [2, 3, 1]]

