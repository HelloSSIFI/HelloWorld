from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
mat = [[n*m]*m for _ in range(n)]

direct = [(1, 0), (1, 1), (1, -1), (0, 1), (0, -1), (-1, 0), (-1, 1), (-1, -1)]

baby = []
for a in range(n):
    for b in range(m):
        if arr[a][b]:baby.append((a, b))


result = n*m

for sk in baby:
    visit = [[-1]*m for _ in range(n)]
    visit[sk[0]][sk[1]] = 0
    Q = deque([sk])

    while Q:
        x, y = Q.popleft()

        for d in direct:
            sx, sy = x+d[0], y+d[1]
            if 0 <= sx < n and 0 <= sy < m and arr[sx][sy] != 1 and visit[sx][sy]==-1:
                mat[sx][sy] = min(mat[sx][sy], visit[x][y]+1)
                visit[sx][sy] = visit[x][y]+1
                Q.append((sx, sy))


result = 0
for a in range(n):
    for b in range(m):
        if mat[a][b] != n*m:
            result = max(result, mat[a][b])

print(result)