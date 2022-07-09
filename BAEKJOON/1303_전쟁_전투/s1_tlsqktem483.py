import sys


def dfs(r, c, team):
    global visited
    di = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 상 우 하 좌
    n = 0

    visited[r][c] = True
    stack = [(r, c)]
    while stack:
        (i, j) = stack.pop()
        for d in di:
            next_i, next_j = i + d[0], j + d[1]
            if 0 <= next_i < M and 0 <= next_j < N and war[next_i][next_j] == team and not visited[next_i][next_j]:
                n += 1
                visited[next_i][next_j] = True
                stack.append((next_i, next_j))
    return n + 1


N, M = map(int, sys.stdin.readline().split())
war = [sys.stdin.readline() for _ in range(M)]
visited = [[False]*N for _ in range(M)]

w, b = 0, 0

for i in range(M):
    for j in range(N):
        if war[i][j] == 'W' and not visited[i][j]:
            w += dfs(i, j, 'W') ** 2
        elif war[i][j] == 'B' and not visited[i][j]:
            b += dfs(i, j, 'B') ** 2

print(w, b)