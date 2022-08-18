from collections import deque
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
x1, y1, x2, y2 = map(lambda x:x-1, map(int, input().split()))
visit = [[float('inf')]*m for _ in range(n)]
visit[x1][y1] = 0

direct = [(0, 1), (1, 0), (0, -1), (-1, 0)]
Q = deque([(x1, y1)])

while Q:
    x, y = Q.popleft()

    if x == x2 and y == y2:
        continue

    for d in direct:
        for p in range(1, k+1):
            sx, sy = x+d[0]*p, y+d[1]*p
            if 0 <= sx < n and 0 <= sy < m and arr[sx][sy] == '.' and visit[sx][sy] > visit[x][y]:
                if visit[sx][sy]==float('inf'):
                    Q.append((sx, sy))
                    visit[sx][sy] = visit[x][y]+1
            else:
                break

print(visit[x2][y2] if visit[x2][y2] != float('inf') else -1)