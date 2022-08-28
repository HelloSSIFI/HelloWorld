from collections import deque

def solution(n, road, k):
    answer = 0

    graph = [[] for _ in range(n+1)]
    for a, b, c in road:
        graph[a].append([b, c])
        graph[b].append([a, c])

    dist = [float('inf') for _ in range(n+1)]
    dist[1] = 0
    # visit = [0 for _ in range(n+1)]
    # visit[1] = 1

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

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3))
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4))