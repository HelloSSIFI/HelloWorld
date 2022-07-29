from collections import deque
import sys
input = sys.stdin.readline


for tc in range(int(input())):
    # 건물 개수,건설 순서 규칙 K 개
    N, K = map(int, input().split())

    #각 건물당 건설 시간 N 개
    constr = list(map(int, input().split()))

    graph = [[] for i in range(N)]
    degree = [0]*N
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        degree[b-1] += 1

    win = int(input())-1

    DP = [0]*N
    Q = deque([])
    for i in range(N):
        if degree[i] == 0:
            Q.append(i)
            DP[i] += constr[i]

    while Q:
        now = Q.popleft()

        for j in graph[now]:
            degree[j] -= 1
            DP[j] = max(DP[j], DP[now]+constr[j])

            if degree[j]==0:
                Q.append(j)


    print(DP[win])