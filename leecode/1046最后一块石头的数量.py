from queue import PriorityQueue
class Solution:
    def lastStoneWeight(self, stones):
        # print(sorted(stones, reverse=True)[:2])
        s_list = sorted(stones, reverse=True)
        while len(s_list) >= 2:
            print(s_list)
            s_list = sorted(s_list, reverse=True)
            if s_list[0] == s_list[1]:
                s_list.pop(0)
                s_list.pop(1)
            else:
                s_list[0] -= s_list[1]
                s_list.pop(1)
        # return s_list[0]



if __name__ == '__main__':
    # lists = [32, 35, 39, 30, 88, 67, 52, 80]
    # lists.pop(1)
    # print(lists)
    s = Solution()
    s.lastStoneWeight([2, 2])
