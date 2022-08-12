import sys
from collections import deque
input = sys.stdin.readline

graph = [list(input()) for _ in range(12)]
visited = [[False]*6 for _ in range(12)]
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]
ans = 0


def boom(r, c, target):
    global visited, check

    queue = deque()
    queue.append([r, c])
    check.append([r, c])

    while queue:
        i, j = queue.popleft()
        for d in di:
            ni, nj = i + d[0], j + d[1]

            if 0 <= ni < 12 and 0 <= nj < 6 and graph[ni][nj] == target and not visited[ni][nj]:
                visited[ni][nj] = True
                queue.append([ni, nj])
                check.append([ni, nj])


def arrange():
    global graph

    for j in range(6):
        for i in range(10, -1, -1):
            for k in range(11, i, -1):
                if graph[i][j] != '.' and graph[k][j] == '.':
                    graph[k][j] = graph[i][j]
                    graph[i][j] = '.'
                    break


is_boom = True
while is_boom:
    is_boom = False
    visited = [[False] * 6 for _ in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not visited[i][j]:
                visited[i][j] = True
                check = []
                boom(i, j, graph[i][j])
                if len(check) > 3:
                    is_boom = True
                    for r, c in check:
                        graph[r][c] = '.'

    if is_boom:
        arrange()
        ans += 1

print(ans)