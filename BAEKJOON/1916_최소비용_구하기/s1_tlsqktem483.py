"""
Dijkstra 알고리즘
우선순위 Queue

pypy3 에서는 통과 : 388ms
python 에서는 시간초과
"""
from heapq import heappush, heappop

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

s, e = map(int, input().split())
inf = int(1e9)
d = [inf] * (n+1)


def dijkstra(start):
    q = [(0, start)]
    d[start] = 0

    while q:
        dist, node = heappop(q)
        if d[node] < dist:
            continue
        for next in graph[node]:
            cost = d[node] + next[1]

            if cost < d[next[0]]:
                d[next[0]] = cost
                heappush(q, (cost, next[0]))


dijkstra(s)
print(d[e])