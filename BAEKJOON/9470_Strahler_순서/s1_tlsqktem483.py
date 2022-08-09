import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    K, M, P = map(int, input().split())
    degree = [[0, 0, 0] for _ in range(M+1)]
    graph = [[] for _ in range(M+1)]

    for _ in range(P):
        s, e = map(int, input().split())
        graph[s].append(e)
        degree[e][0] += 1

    queue = deque()
    for i in range(1, M+1):
        if degree[i][0] == 0:
            queue.append(i)
            degree[i][1] = 1

    while queue:
        now = queue.popleft()

        for next in graph[now]:
            degree[next][0] -= 1
            if degree[next][1] < degree[now][1]:
                degree[next][1] = degree[now][1]
                degree[next][2] = 1
            elif degree[next][1] == degree[now][1]:
                degree[next][2] += 1

            if degree[next][0] == 0:
                if degree[next][2] > 1:
                    degree[next][1] += 1
                queue.append(next)

    print(K, degree[M][1])