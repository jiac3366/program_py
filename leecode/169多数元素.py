class Solution:
    def majorityElement(self, nums):
        lens = len(nums)
        from collections import Counter
        c = Counter(nums).most_common()
        return [i[0] for i in c]


if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([1]))
