# 참고: https://kimjingo.tistory.com/155

def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])

    # 누적합을 저장할 배열
    field = [[0 for _ in range(m+1)] for _ in range(n+1)]

    for ty, r1, c1, r2, c2, deg in skill:
        field[r1][c1] += -deg if ty == 1 else deg
        field[r1][c2+1] += deg if ty == 1 else -deg
        field[r2+1][c1] += deg if ty == 1 else -deg
        field[r2+1][c2+1] += -deg if ty == 1 else deg

    for i in range(n):
        for j in range(m-1):
            field[i][j+1] += field[i][j]

    for i in range(m):
        for j in range(n-1):
            field[j+1][i] += field[j][i]

    for i in range(n):
        for j in range(m):
            board[i][j] += field[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer