class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s1 = [0] * 26
        s2 = [0] * 26
        for i in s:
            s1[ord(i) - ord('a')] += 1
        for i in t:
            s2[ord(i) - ord('a')] += 1
        return s1 == s2


if __name__ == '__main__':
    s = Solution()
    s.isAnagram('nagaram', 'anagram')
