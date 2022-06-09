import heapq

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
money = [9876543210] * (N+1)

for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    money[start] = 0

    while q:
        temp, node = heapq.heappop(q)

        if money[node] < temp:
            continue

        for i in graph[node]:
            cost = temp + i[1]
            if cost < money[i[0]]:
                money[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(start)
print(money)
print(money[end])



