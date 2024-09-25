def solution(board):
    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                o_cnt += 1
            if board[i][j] == "X":
                x_cnt += 1

    if o_cnt < x_cnt:
        return 0
    elif o_cnt - x_cnt > 1:
        return 0

    result = set()
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            result.add(board[i][0])

        elif board[0][i] == board[1][i] == board[2][i]:
            result.add(board[0][i])

    if board[0][0] == board[1][1] == board[2][2]:
        result.add(board[0][0])
    if board[0][2] == board[1][1] == board[2][0]:
        result.add(board[0][2])

    if result == {}:
        return 0

    if o_cnt == x_cnt and "O" in result:
        return 0

    if o_cnt > x_cnt and "X" in result:
        return 0

    if "X" in result and "O" in result:
        return 0

    return 1
