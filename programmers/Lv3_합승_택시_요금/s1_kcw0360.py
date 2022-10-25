import heapq


def dijkstra(start, arr, graph):
    heap = []
    arr[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        fare, now = heapq.heappop(heap)

        if fare > arr[now]:
            continue
        else:
            arr[now] = fare

        for nxt, nf in graph[now]:
            heapq.heappush(heap, (fare + nf, nxt))

    return arr


def solution(n, s, a, b, fares):
    answer = 10**9
    graph = [[] for _ in range(n+1)]

    for q, w, e in fares:
        graph[q].append([w, e])
        graph[w].append([q, e])

    check = dijkstra(s, [10**9] * (n+1), graph)

    for st in range(1, n+1):
        temp = dijkstra(st, [10**9] * (n+1), graph)
        answer = min(answer, check[st] + temp[a] + temp[b])

    return answer