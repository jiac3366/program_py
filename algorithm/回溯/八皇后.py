import copy
class Solution:
    def solveNQueens(self, n):
        self.res = []
        self.board = [["." for _ in range(n)] for i in range(n)]

        # 可选列表是根据board推导出来的：条件是 "每个皇后都不同行、不同列，也不在对角线上"
        # row 阶段
        # path board
        def backtrack(row, board, n):
            if row == n:
                item_board = copy.deepcopy(board)
                item_board = [''.join(item) for item in item_board]
                self.res.append(item_board)
                return

            for col in range(n):
                if isOK(board, row, col, n):
                    board[row][col] = 'Q'
                    backtrack(row + 1, board, n)
                    board[row][col] = '.'

        # 判断row行和col列是否放置合适
        def isOK(board, row, col, n):

            # 判断这1列有没有-->0-row-1行/col列
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # 判断右上角有没有Q
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            # 判断左上角有没有Q
            i = row - 1
            j = col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            return True

        backtrack(0, self.board, n)
        return self.res


if __name__ == '__main__':
    c = Solution()
    print(c.solveNQueens(4))
    # s = '....'
    # s[2] = 'O'
