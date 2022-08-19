import sys
from collections import deque
input = sys.stdin.readline

# 상, 하, 좌, 우, 대각 왼 위, 대각 오른 위, 대각 오른 아래
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]]         

N, M = map(int, input().split())
shark_map = [list(map(int, input().split())) for _ in range(N)]
dist_map = [[0] * M for _ in range(N)]
sharks = []
for i in range(N):
    for j in range(M):
        if shark_map[i][j]:
            sharks.append((0, i, j))                 # (거리, x좌표, y좌표)

q = deque(sharks)

while q:
    dist, r, c = q.popleft()
    for n in dirs:
        nr = r + n[0]
        nc = c + n[1]
        if 0 <= nr < N and 0 <= nc < M and (0, nr, nc) not in sharks:
            if not dist_map[nr][nc] or dist + 1 < dist_map[nr][nc]:
                dist_map[nr][nc] = dist + 1
                q.append((dist + 1, nr, nc))
answer = max(list(map(lambda arr : max(arr), dist_map)))
print(answer)