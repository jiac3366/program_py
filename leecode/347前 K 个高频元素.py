class Solution:
    def topKFrequent(self, nums, k):
        from collections import Counter
        c = Counter(nums).most_common(k)
        return [i[0] for i in c]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
