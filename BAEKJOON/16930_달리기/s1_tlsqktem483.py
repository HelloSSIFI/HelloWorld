import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
gym = [list(input()) for _ in range(N)]
visited = [[float('inf')] * M for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1

queue = deque()
queue.append((x1, y1))
visited[x1][y1] = 0

while queue:
    i, j = queue.popleft()

    for (di, dj) in d:
        ni = i + di
        nj = j + dj
        cnt = 1

        # 한방향으로 계속 이동
        while cnt <= K and 0 <= ni < N and 0 <= nj < M and gym[ni][nj] != '#' and visited[ni][nj] > visited[i][j]:
            if visited[ni][nj] == float('inf'):
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
            ni += di
            nj += dj
            cnt += 1

if visited[x2][y2] == float('inf'):
    print(-1)
else:
    print(visited[x2][y2])

