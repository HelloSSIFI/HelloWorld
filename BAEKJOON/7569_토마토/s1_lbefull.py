from collections import deque
import sys
input = sys.stdin.readline


def bfs():
    max_day = 0
    while Q:
        h, r, c, day = Q.popleft()
        if max_day < day: max_day = day                     # day가 최대값보다 커질경우 갱신
        for d in range(6):                                  # 6방향 탐색
            nh = h + dh[d]                                  # 안익은 토마토가 인접해있으면
            nr = r + dr[d]                                  # 익은 토마토로 변경 후 Q에 넣어줌
            nc = c + dc[d]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = 1
                Q.append((nh, nr, nc, day + 1))

    return max_day


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
dr = [1, -1, 0, 0, 0, 0]
dc = [0, 0, 1, -1, 0, 0]
dh = [0, 0, 0, 0, 1, -1]
Q = deque()
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 1:                           # 익은 토마토 위치를 Q에 저장
                Q.append((h, r, c, 0))

answer = bfs()                                              # BFS 탐색
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arr[h][r][c] == 0:                           # 안익은 토마토가 남았으면 -1
                answer = -1

print(answer)
