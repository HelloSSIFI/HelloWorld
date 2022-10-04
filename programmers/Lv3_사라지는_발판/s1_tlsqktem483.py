"""
MinMax Tree
"""
from copy import deepcopy
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
def A_turn(ai, aj, bi, bj, cnt, board):
    if board[ai][aj] == 0:
        return (1, cnt)
    win = []
    lose = []
    flag = False

    for di in d:
        ni, nj = ai + di[0], aj + di[1]

        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 1:
            flag = True
            temp = deepcopy(board)
            temp[ai][aj] = 0
            is_win, turn = B_turn(bi, bj, ni, nj, cnt+1, temp)
            if is_win:
                win.append(turn)
            else:
                lose.append(turn)
    if flag:
        if win:
            return (0, min(win))
        else:
            return (1, max(lose))
    else:
        return (1, cnt)


def B_turn(bi, bj, ai, aj, cnt, board):
    if board[bi][bj] == 0:
        return (1, cnt)
    win = []
    lose = []
    flag = False

    for di in d:
        ni, nj = bi + di[0], bj + di[1]

        if 0 <= ni < len(board) and 0 <= nj < len(board[0]) and board[ni][nj] == 1:
            flag = True
            temp = deepcopy(board)
            temp[bi][bj] = 0
            is_win, turn = A_turn(ai, aj, ni, nj, cnt + 1, temp)
            if is_win:
                win.append(turn)
            else:
                lose.append(turn)
    if flag:
        if win:
            return (0, min(win))
        else:
            return (1, max(lose))
    else:
        return (1, cnt)


def solution(board, aloc, bloc):
    ai, aj, bi, bj = aloc[0], aloc[1], bloc[0], bloc[1]
    return A_turn(ai, aj, bi, bj, 0, board)[1]


print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print(solution([[1]], [0, 0], [0, 0]))