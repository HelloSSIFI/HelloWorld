import copy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = 0


def up(copy_board):
    for j in range(N):
        p = 0
        for i in range(1, N):
            if copy_board[i][j]:
                tmp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[p][j] == 0:
                    copy_board[p][j] = tmp

                elif copy_board[p][j] == tmp:
                    copy_board[p][j] *= 2
                    p += 1

                else:
                    p += 1
                    copy_board[p][j] = tmp

    return copy_board


def down(copy_board):
    for j in range(N):
        p = N-1
        for i in range(N-2, -1, -1):
            if copy_board[i][j]:
                tmp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[p][j] == 0:
                    copy_board[p][j] = tmp

                elif copy_board[p][j] == tmp:
                    copy_board[p][j] *= 2
                    p -= 1

                else:
                    p -= 1
                    copy_board[p][j] = tmp

    return copy_board


def left(copy_board):
    for i in range(N):
        p = 0
        for j in range(1, N):
            if copy_board[i][j]:
                tmp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[i][p] == 0:
                    copy_board[i][p] = tmp

                elif copy_board[i][p] == tmp:
                    copy_board[i][p] *= 2
                    p += 1

                else:
                    p += 1
                    copy_board[i][p] = tmp

    return copy_board


def right(copy_board):
    for i in range(N):
        p = N-1
        for j in range(N-2, -1, -1):
            if copy_board[i][j]:
                tmp = copy_board[i][j]
                copy_board[i][j] = 0

                if copy_board[i][p] == 0:
                    copy_board[i][p] = tmp

                elif copy_board[i][p] == tmp:
                    copy_board[i][p] *= 2
                    p -= 1

                else:
                    p -= 1
                    copy_board[i][p] = tmp

    return copy_board


def game(board, cnt):
    global answer

    if cnt == 5:
        for i in range(N):
            answer = max(answer, max(board[i]))
        return

    game(up(copy.deepcopy(board)), cnt + 1)
    game(down(copy.deepcopy(board)), cnt + 1)
    game(left(copy.deepcopy(board)), cnt + 1)
    game(right(copy.deepcopy(board)), cnt + 1)

game(board, 0)

print(answer)