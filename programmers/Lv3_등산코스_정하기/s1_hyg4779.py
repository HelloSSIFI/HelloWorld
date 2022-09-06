from collections import deque

def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])


    dist = [10000001 for _ in range(n+1)]
    for gate in gates:
        dist[gate] = 0

    Q = deque(gates)
    while Q:
        now = Q.popleft()
        if now in summits: continue
        for node, cost in graph[now]:
            cost = max(dist[now], cost)
            if dist[node] > cost:
                Q.append(node)
                dist[node] = cost


    min_dis = float('inf')
    min_summit = -1

    for summit in summits:
        if min_dis > dist[summit]:
            min_dis = dist[summit]
            min_summit = summit
        elif min_dis == dist[summit] and min_summit > summit:
            min_summit = summit

    return [min_summit, min_dis]


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))