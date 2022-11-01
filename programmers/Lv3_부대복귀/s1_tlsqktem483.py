"""
N <= 100,000
heapq 활용한 Dijkstra
"""
import heapq
from collections import defaultdict


def solution(n, roads, sources, destination):
    answer = []
    graph = defaultdict(list)
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)
    distance = [float('inf') for _ in range(n+1)]
    distance[destination] = 0
    q = []
    heapq.heappush(q, [destination, distance[destination]])

    while q:
        cur, dist = heapq.heappop(q)

        if distance[cur] < dist:
            continue

        for n_node in graph[cur]:
            if distance[n_node] > dist+1:
                distance[n_node] = dist+1
                heapq.heappush(q, [n_node, dist+1])

    for loc in sources:
        temp = -1 if distance[loc] == float('inf') else distance[loc]
        answer.append(temp)
    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))