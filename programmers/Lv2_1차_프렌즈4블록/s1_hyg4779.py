def solution(m, n, board):  # 높이m, 폭n

    board = [list(line) for line in board]
    answer = 0

    while True:
        boom = set()

        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]:
                    tmp = board[i][j]
                    if tmp == board[i][j+1] == board[i+1][j] == board[i+1][j+1]:
                        boom.update({(i, j), (i, j+1), (i+1, j), (i+1, j+1)})

        if boom:

            for b in boom:
                board[b[0]][b[1]] = False
                answer += 1

            while True:
                flag = True
                for i in range(m-1):
                    for j in range(n):
                        if board[i][j] and not board[i+1][j]:
                            board[i+1][j], board[i][j] = board[i][j],  board[i+1][j]
                            flag = False
                if flag:
                    break

        else:
            break

    return answer


print(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))