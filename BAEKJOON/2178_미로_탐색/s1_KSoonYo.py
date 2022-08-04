import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
maze = [list(input().strip()) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * M for _ in range(N)]
start = (0, 0)
end = (N - 1, M - 1)

visited[start[0]][start[1]] = 1
q = deque([start])
while q:
    r, c = q.popleft()
    
    if (r, c) == end:
        break

    for i in range(4):
        nr = r + dx[i]
        nc = c + dy[i]

        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] == '1':
            if not visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

print(visited[N - 1][M - 1])
