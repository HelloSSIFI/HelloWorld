import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1)]
queue = deque([])

for r in range(N):
    for c in range(M):
        if graph[r][c] == 1:
            queue.append((r, c))

ans = 0
while queue:
    (i, j) = queue.popleft()
    ans = max(ans, graph[i][j])

    for (di, dj) in d:
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and graph[ni][nj] == 0:
            queue.append((ni, nj))
            graph[ni][nj] = graph[i][j] + 1

print(ans-1)