import sys
from collections import deque
input = sys.stdin.readline
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(r, c, power, eat):
    global t, graph

    q = deque()
    q.append([r, c, 0])
    visited = [[False]*N for _ in range(N)]
    visited[r][c] = True
    dist = N*N+1
    target = [0, 0]

    while q:
        i, j, cnt = q.popleft()

        if cnt > dist:
            continue

        if graph[i][j] != 9 and 0 < graph[i][j] < power:
            if cnt < dist:
                dist = cnt
                target = [i, j]
            elif cnt == dist:
                if i < target[0]:
                    target = [i, j]
                elif i == target[0] and j < target[1]:
                    target = [i, j]

        for di in d:
            ni, nj = i + di[0], j + di[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and graph[ni][nj] <= power:
                q.append([ni, nj, cnt+1])
                visited[ni][nj] = True
    if dist == N*N+1:
        return r, c, power, eat
    else:
        graph[r][c] = 0
        graph[target[0]][target[1]] = 9
        t += dist
        eat += 1
        if eat == power:
            power += 1
            eat = 0

        return target[0], target[1], power, eat


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == 9:
            s = [i, j, 2]
t = 0
i, j, p, e = s[0], s[1], s[2], 0
while True:
    ni, nj, np, ne = bfs(i, j, p, e)
    if i == ni and j == nj:
        break
    i, j, p, e = ni, nj, np, ne

print(t)