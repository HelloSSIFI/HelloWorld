"""
BFS + 7개 키 ord 의 visited
"""
import sys
from collections import deque
input = sys.stdin.readline


def bfs(s):
    q = deque()
    q.append([s[0], s[1], 0, 0])
    visited[s[0]][s[1]][0] = True

    while q:
        i, j, k, cnt = q.popleft()

        for di in d:
            ni, nj = i + di[0], j + di[1]

            if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj][k] and graph[ni][nj] != '#':
                if graph[ni][nj] == '.' or graph[ni][nj] == '0':
                    visited[ni][nj][k] = True
                    q.append([ni, nj, k, cnt+1])
                elif graph[ni][nj] == '1':
                    return cnt + 1
                elif graph[ni][nj].islower():
                    nk = k | (1 << ord(graph[ni][nj]) - 97)
                    if not visited[ni][nj][nk]:
                        visited[ni][nj][nk] = True
                        q.append([ni, nj, nk, cnt+1])
                elif graph[ni][nj].isupper():
                    if k & 1 << (ord(graph[ni][nj]) - 65):
                        visited[ni][nj][k] = True
                        q.append([ni, nj, k, cnt+1])
    return -1


N, M = map(int, input().split())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
graph = [list(input()) for _ in range(N)]
visited = [[[False]*64 for _ in range(M)] for _ in range(N)]
start = (0, 0)
ans = float('inf')

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            start = (i, j)

print(bfs(start))