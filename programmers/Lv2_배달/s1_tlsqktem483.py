"""
다익스트라
"""
import heapq
from collections import defaultdict


def solution(N, road, K):
    start = 0
    answer = 0
    graph = defaultdict(list)
    for s, e, d in road:
        graph[s - 1].append([e - 1, d])
        graph[e - 1].append([s - 1, d])
    distance = {node: float('inf') for node in range(N)}
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [distance[start], start])

    while queue:
        d, node = heapq.heappop(queue)

        if distance[node] < d:
            continue

        for n_node, n_d in graph[node]:
            di = d + n_d
            if di < distance[n_node]:
                distance[n_node] = di
                heapq.heappush(queue, [di, n_node])

    for d in distance.values():
        if d <= K:
            answer += 1
    return answer


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))