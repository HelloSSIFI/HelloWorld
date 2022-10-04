# 참고: https://sujeng97.tistory.com/36
'''
def solution(board, aloc, bloc):
    answer = 15
    n, m = len(board), len(board[0])
    direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # visit = [[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]

    def dfs(A, B, cnt):
        nonlocal answer
        r1, c1 = A
        r2, c2 = B

        # a와 b의 이동유무
        a_flag, b_flag = False, False
        if board[r1][c1] == 0 or board[r2][c2] == 0:
            answer = min(answer, cnt)
            return

        # A 이동
        for da in direct:
            nr1, nc1 = r1+da[0], c1+da[1]
            if 0 <= nr1 < n and 0 <= nc1 < m and board[nr1][nc1] == 1:
                board[r1][c1] = 0
                a_flag = True

                # B의 위치가 0이 됐다면 승자 A 리턴
                if board[r2][c2] == 0:
                    answer = min(answer, cnt+1)
                    board[r1][c1] = 1
                    continue

                # B 이동
                for db in direct:
                    nr2, nc2 = r2+db[0], c2+db[1]
                    if 0 <= nr2 < n and 0 <= nc2 < m and board[nr2][nc2] == 1:
                        board[r2][c2] = 0
                        b_flag = True

                        # 이동한 A의 위치가 0이  됐다면 승자 B 리턴
                        if board[nr1][nc1] == 0:
                            board[r2][c2] = 1
                            answer = min(answer, cnt+2)
                            continue

                        dfs((nr1, nc1), (nr2, nc2), cnt+2)
                        board[r2][c2] = 1


                # B가 이동하지 못했다면 승자 A
                if b_flag == False:
                    answer = min(answer, cnt+1)

                # 이동해서 사라진 이전 A 발판 복구
                board[r1][c1] = 1

        # A가 이동 못했다면 승자 B
        if a_flag == False:
            answer = min(answer, cnt)

    dfs(aloc, bloc, 0)
    return answer
'''
direct = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def A_turn(ar, ac, br, bc, cnt, board):
    # A가 0이 됐으면 B가 이긴것
    if board[ar][ac] == 0:
        return (1, cnt)

    # 이겼을 때 이동 횟수
    winner = []
    # 졌을때 이동 횟수
    loser = []
    # 이동했는지 여부
    flag = False
    for d in direct:
        nr, nc = ar+d[0], ac+d[1]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [line[:] for line in board]
            temp[ar][ac] = 0
            # 승패 여부, 이동 횟수
            iswin, turn = B_turn(br, bc, nr, nc, cnt+1, temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)

    # 이동 했을 때
    if flag:
        # 이긴 적이 있으면 이겼을 때 최소 이동 횟수 return
        if winner:
            return (0, min(winner))
        # 이긴 적이 없으면 졌을 때 최대 이동 횟수 return
        else:
            return (1, max(loser))

    # 이동 못했으면 상대가 이긴것
    else:
        return (1, cnt)

def B_turn(br, bc, ar, ac, cnt, board):
    if board[br][bc] == 0:
        return (1, cnt)

    winner = []
    loser = []
    flag = False

    for d in direct:
        nr, nc = br+d[0], bc+d[1]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 1:
            flag = True
            temp = [line[:] for line in board]
            temp[br][bc] = 0
            iswin, turn = A_turn(ar, ac, nr, nc, cnt+1, temp)
            if iswin:
                winner.append(turn)
            else:
                loser.append(turn)

    if flag:
        if winner:
            return (0, min(winner))
        else:
            return (1, max(loser))

    else:
        return (1, cnt)

def solution(board, aloc, bloc):
    ar, ac = aloc
    br, bc = bloc
    answer = A_turn(ar, ac, br, bc, 0, board)[1]
    return answer

print(solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [1, 0], [1, 2]))
print(solution([[1, 1, 1, 1, 1]], [0, 0], [0, 4]))
print(solution([[1]], [0, 0], [0, 0]))