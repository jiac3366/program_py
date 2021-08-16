class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        lists = []
        self._gen(lists, 0, 0, n, "")

    def _gen(self, lists, left, right, max, strs):
        if left == max and right == max:
            lists.append(strs)
            print(lists)
            return

        if left < max:
            self._gen(lists, left + 1, right, max, strs + '(')

        if right < left:
            self._gen(lists, left, right + 1, max, strs + ')')


class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        # 错误做法
        def helper(res, strs, left, right, n):
            if left == n and right == n:
                res.append(strs)
                print(res)
                return
            if left < n:
                strs += '('
                helper(res, strs, left + 1, right, n)
            if right < left:
                strs += ')'
                helper(res, strs, left, right + 1, n)

        helper(res, '', 0, 0, n)
        # return res


if __name__ == '__main__':
    s = Solution()
    s.generateParenthesis(3)

    print("----------------")
    # 错误做法
    a = Solution2()
    a.generateParenthesis(3)

