"""
BFS
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 상 우 하 좌
graph = []

for _ in range(N):
    graph.append(list(input().rstrip()))


def bfs(i, j):
    global graph

    queue = [(i, j)]

    while queue:
        (r, c) = queue.pop(0)

        for d in di:
            next_r, next_c = r + d[0], c + d[1]

            if 0 <= next_r < N and 0 <= next_c < M and graph[next_r][next_c] == "1":
                graph[next_r][next_c] = int(graph[r][c]) + 1
                queue.append((next_r, next_c))

    return graph[N-1][M-1]

print(bfs(0, 0))