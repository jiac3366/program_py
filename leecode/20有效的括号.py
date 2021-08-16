class Solution(object):
    # 错误的做法
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s is None or s == "":
            return False

        if len(s) % 2 == 1:
            return False
        maps = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        left_stack = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                left_stack.append(i)
            if i == "}" or i == "]" or i == ")":
                strs = left_stack.pop()
                if maps[i] != strs:
                    return False
        if len(left_stack) != 0:
            return False
        return True

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False

        if len(s) % 2 == 1:
            return False
        maps = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        left_stack = []
        for i in s:
            if i in maps.values():
                left_stack.append(i)
            elif i in maps.keys():
                if left_stack == [] or maps[i] != left_stack.pop():  # 注意这里要先检查是否为空 再弹出栈
                    return False
            else:
                return False
        return left_stack == []


if __name__ == '__main__':
    stack = [1, 2, 3, 54, 6, 7]
