from typing import List, Set


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.helper(nums, res, [], 0)
        return list(res)

    def helper(self, nums: List, result: List, path: List, start: int):
        if start == 3:
            result.append(path[:])
            return

        for i in range(start, len(nums)):

            path.append(nums[i])
            self.helper(nums, result, path, i )
            path.pop()
        return


if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
]
