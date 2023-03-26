from collections import deque


import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n: 한 변의 크기, m: 색상의 개수

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
while True:
    visited = [[0]*n for _ in range(n)]
    check = []
    for i in range(n):
        for j in range(n):
            if board[i][j] <= 0 or visited[i][j] == 1:    # 시작점이 한번 방문한 곳이거나 무지개 블록 혹은 검은색 블록은 pass
                continue

            visited[i][j] = 1
            temp_n = [[i, j]]    # 일반 블록 위치
            temp_r = []    # 무지개 블록 위치는 방문 복구를 하기위해 따로 저장
            total = 1    # 블록의 총 개수
            rainbow = 0    # 무지개 블록만 따로 체크
            q = deque([[i, j]])

            while q:
                a, b = q.popleft()
                for k in range(4):
                    y = a + dy[k]
                    x = b + dx[k]
                    if 0 <= y < n and 0 <= x < n and visited[y][x] == 0 and (board[y][x] == 0 or board[y][x] == board[i][j]):
                        q.append([y, x])
                        visited[y][x] = 1
                        if board[y][x] == board[i][j]:
                            total += 1
                            temp_n.append([y, x])
                        else:
                            total += 1
                            rainbow += 1
                            temp_r.append([y, x])

            for ty, tx in temp_r:    # 무지개는 다른 블록 그룹에도 포함될 수 있기 때문에 방문 복구
                visited[ty][tx] = 0

            if total >= 2:
                check.append([total, rainbow, temp_n + temp_r])
    check.sort(reverse=True)    # 조건 1에 맞춰 정렬 (블록 수, 무지개 블록 수, 행, 열)

    if check:    # 블록그룹이 존재하면 조건에 만족하는 블록제거
        for a, b in check[0][2]:
            board[a][b] = -2
        answer += check[0][0]**2    # 제거한 블록의 점수 추가
    else:    # 블록그룹이 없는 경우 반복문 빠져나가기
        break

    for i in range(n-2, -1, -1):    # 중력
        for j in range(n):
            if board[i][j] > -1:
                y = i
                while True:
                    if 0 <= y+1 < n and board[y+1][j] == -2:
                        board[y+1][j] = board[y][j]
                        board[y][j] = -2
                        y += 1
                    else:
                        break

    new_board = list(map(list, zip(*board)))[::-1]   # 반시계 방향으로 90도 회전한 보드
    board = new_board    # 덮어쓰기

    for i in range(n-2, -1, -1):    # 중력
        for j in range(n):
            if board[i][j] > -1:
                y = i
                while True:
                    if 0 <= y+1 < n and board[y+1][j] == -2:
                        board[y+1][j] = board[y][j]
                        board[y][j] = -2
                        y += 1
                    else:
                        break

print(answer)