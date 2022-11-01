from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        s, e = road
        graph[s].append(e)
        graph[e].append(s)


    # 목적지에서 출발하여 bfs로 최단거리 찾기
    dist = [float('inf')] * (n + 1)
    dist[destination] = 0
    q = deque([destination])
    while q:
        s = q.popleft()

        for next in graph[s]:
            if dist[next] > dist[s] + 1:
                dist[next] = dist[s] + 1
                q.append(next)
    
    for source in sources:
        if dist[source] == float('inf'):
            answer.append(-1)
        else:
            answer.append(dist[source])
    return answer




### 시간초과
# import heapq

# def dijkstra(n, src, dest, graph):
#     dist = [float('inf')] * (n + 1)
#     dist[src] = 0
#     q = [(0, src)]                              # (걸린 시간, 출발지)                     
#     while q:
#         costs, here = heapq.heappop(q)

#         if dist[here] < costs:
#             if here == dest:
#                 return dist[here]
#             continue
        
#         for next in graph[here]:
#             if dist[next] > costs + 1:
#                 dist[next] = costs + 1
#                 heapq.heappush(q, (costs + 1, next))
#     return dist[dest]

# def solution(n, roads, sources, destination):
#     answer = []
#     graph = [[] for _ in range(n + 1)]

#     for road in roads:
#         s, e = road
#         graph[s].append(e)
#         graph[e].append(s)

#     for source in sources:
#         if source == destination:
#             answer.append(0)
#         else:
#             distance = dijkstra(n, source, destination, graph)    
#             if distance == float('inf'):
#                 answer.append(-1)
#             else:
#                 answer.append(distance)
#     return answer


# solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5)
