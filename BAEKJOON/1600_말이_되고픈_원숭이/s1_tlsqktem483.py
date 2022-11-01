"""
BFS + 3차원 visited
"""
from collections import deque


def move_list_horse(r, c):
    return [[r-2, c+1], [r-1, c+2], [r+1, c+2], [r+2, c+1], [r+2, c-1], [r+1, c-2], [r-1, c-2], [r-2, c-1]]


def bfs(r, c):

    q = deque()
    visited = [[[0]*(K+1) for _ in range(W)] for _ in range(H)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    q.append([r, c, K])

    while q:
        i, j, k = q.popleft()

        if [i, j] == [end_i, end_j]:
            return visited[i][j][k]

        if k:
            for ni, nj in move_list_horse(i, j):
                if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj][k-1] and not graph[ni][nj]:
                    visited[ni][nj][k-1] = visited[i][j][k] + 1
                    q.append([ni, nj, k-1])

        for di in d:
            ni, nj = i + di[0], j + di[1]

            if 0 <= ni < H and 0 <= nj < W and not visited[ni][nj][k] and not graph[ni][nj]:
                visited[ni][nj][k] = visited[i][j][k] + 1
                q.append([ni, nj, k])

    return -1


K = int(input())
W, H = map(int, input().split())
start_i, start_j, end_i, end_j = 0, 0, H-1, W-1

graph = [list(map(int, input().split())) for _ in range(H)]

print(bfs(start_i, start_j))