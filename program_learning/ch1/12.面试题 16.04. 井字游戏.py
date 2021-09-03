# -*- coding: utf-8 -*-
def tictactoe(board):

    count = 0
    for i in "".join(board):
        if i != " ":
            count += 1

    if count < 9:
        return "Pending"
    return "Draw"


if __name__ == '__main__':
    tictactoe([" OOO","    ","OXXX","XX O"])
