"""
다익스트라
* 입구를 sort 해줘야 함
"""
from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    ans = [0, float('inf')]
    graph = defaultdict(list)
    summits = sorted(summits)

    for s, e, di in paths:
        graph[s].append([e, di])
        graph[e].append([s, di])

    q = []
    d = [float('inf') for _ in range(n+1)]

    for gate in gates:
        d[gate] = 0
        for n_node, distance in graph[gate]:
            heapq.heappush(q, [n_node, distance])

    while q:
        node, distance = heapq.heappop(q)
        if d[node] <= distance:
            continue
        d[node] = distance

        # 산봉우리일 경우
        if node in summits:
            continue

        for n_node, n_dist in graph[node]:
            if d[n_node] <= n_dist:
                continue
            else:
                heapq.heappush(q, [n_node, max(distance, n_dist)])
    dist = float('inf')
    for summit in summits:
        if d[summit] < dist:
            dist = d[summit]
            ans[0], ans[1] = summit, dist
    return ans


print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, 	[[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, 	[[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, 	[[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))