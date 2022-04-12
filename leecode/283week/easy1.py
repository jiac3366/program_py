# coding=utf-8
class Solution:
    def cellsInRange(self, s):
        res = []
        slist = s.split(":")
        c1 = slist[0][0]
        r1 = slist[0][1]
        c2 = slist[1][0]
        r2 = slist[1][1]

        for i in range(ord(c1), ord(c2) + 1):
            for j in range(int(r1), int(r2) + 1):
                res.append(chr(i) + str(j))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.cellsInRange("K1:L2"))
