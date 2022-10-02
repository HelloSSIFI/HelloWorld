def solution(board, skill):
    answer = 0
    R, C = len(board), len(board[0])    # 행 길이, 열 길이
    check = [[0]*(C+1) for _ in range(R+1)]    # 누적 합을 위한 board 생성

    for t, r1, c1, r2, c2, d in skill:    # 누적 합
        if t == 2:
            d = -d
        check[r1][c1] -= d
        check[r2+1][c2+1] -= d
        check[r1][c2+1] += d
        check[r2+1][c1] += d

    for i in range(R):    # 왼쪽에서 오른쪽으로 누적 합 진행
        for j in range(C):
            check[i][j+1] += check[i][j]

    for i in range(R):    # 위에서 아래로 누적 합 진행
        for j in range(C):
            check[i+1][j] += check[i][j]

    for i in range(R):    # 누적 합 된 값과 board에 있는 값의 합이 0보다 큰 경우 찾기
        for j in range(C):
            if board[i][j] + check[i][j] > 0:
                answer += 1

    return answer