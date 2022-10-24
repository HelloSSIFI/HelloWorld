from heapq import heappush, heappop


def solution(n, s, a, b, fares):
    """
    Dijkstra
    """

    def dijkstra(cur):
        q = [[0, cur]]
        dist = [float('inf') for _ in range(n+1)]
        dist[cur] = 0
        while q:
            w, x = heappop(q)
            if dist[x] < w:
                continue
            for y, cost in edges[x]:
                cost += w
                if cost < dist[y]:
                    dist[y] = cost
                    heappush(q, [cost, y])
        return dist

    edges = [[] for _ in range(n + 1)]
    ans = float('inf')

    for start, end, dist in fares:
        edges[start].append([end, dist])
        edges[end].append([start, dist])

    for k in range(1, n + 1):
        distance = dijkstra(k)
        ans = min(ans, distance[s] + distance[a] + distance[b])

    return ans


print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))
