from collections import deque

def solution(n, road, k):
    answer = 0

    graph = [[] for _ in range(n+1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dist = [float('inf') for _ in range(n+1)]
    dist[1] = 0

    Q = deque([1])
    while Q:
        v = Q.popleft()

        for i in graph[v]:
            now, cost = i
            if dist[now] >= cost+dist[v]:
                dist[now] = cost+dist[v]
                Q.append(now)

    for j in dist:
        if j <= k:
            answer += 1

    return answer