import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())                        # N : 가로, M : 세로
zone = [list(input().strip()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
dx, dy  = [-1, 1, 0, 0], [0, 0, -1, 1]
powers = {
    'W' : 0,
    'B' : 0
}
for i in range(M):
    for j in range(N):
        if visited[i][j]:
            continue
        color = zone[i][j]
        q = deque([(i, j)])
        visited[i][j] = 1
        cnt = 1
        while q:
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < M and 0 <= ny < N and zone[nx][ny] == color:
                    if not visited[nx][ny]:
                        visited[nx][ny] = 1
                        cnt += 1
                        q.append((nx, ny))
        powers[color] += cnt ** 2


print(powers['W'], powers['B'])

