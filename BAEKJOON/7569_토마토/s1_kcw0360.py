from collections import deque


M, N, H = map(int, input().split())    # M: 가로, N: 세로, H: 상자의 수

tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

dy = [-1, 1, 0, 0, 0, 0]
dx = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

q = deque()
# 익은 토마토의 위치 q에 추가
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                q.append([h, n, m])

while q:
    z, y, x = q.popleft()
    for k in range(6):
        nz = z + dz[k]
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M:
            if tomato[nz][ny][nx] == 0:    # 익지 않은 토마토인 경우
                tomato[nz][ny][nx] = tomato[z][y][x] + 1    # 이전 토마토에 + 1 값으로 표기 (익은 날짜 체크)
                q.append([nz, ny, nx])


# 가장 늦게 익은 날 찾기
answer = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 0:    # 익지 않은 것이 하나라도 있다면 return -1
                print(-1)
                exit(0)
            answer = max(answer, tomato[h][n][m])

print(answer - 1)