import heapq

def dijkstra(graph, s, n):
    dist = [float('inf')] * (n + 1)
    q = [(0, s)]
    dist[s] = 0

    while q:
        cost, here = heapq.heappop(q)

        if dist[here] < cost:
            continue

        for next_node, next_cost in graph[here]:
            if dist[next_node] > cost + next_cost:
                dist[next_node] = cost + next_cost
                heapq.heappush(q, (cost + next_cost, next_node))
    return dist

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n + 1)]             # [linked node, cost]
    
    for fare in fares:
        start, end, cost = fare
        graph[start].append((end, cost))            
        graph[end].append((start, cost))
    
    together = dijkstra(graph, s, n)               # 같이 출발했을 때, 최단 경로 
    minC = float('inf')
    for node in range(1, n + 1):
        # 현재 node에서 각자 출발 했을 때
        # a, b로 각자 최단 경로로 출발
        individual = dijkstra(graph, node, n)
        toA, toB = individual[a], individual[b]
        minC = min(minC, together[node] + toA + toB)    # 현재 node까지 같이 출발한 후, 현재 node에서 도착지까지 따로 출발했을 때 최소 비용 갱신
    answer = minC
    return answer

solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])




### 틀린 이유 : 도착지와 이어져 있지 않은 간선이 있기 때문에 동반 출발한 비용을 방문할 때마다 더해주면 안된다.
# import heapq

# def dijkstra(graph, s, a, b, n):
#     dist = [float('inf')] * (n + 1)
#     q = [(0, s)]
#     dist[s] = 0

#     while q:
#         cost, here = heapq.heappop(q)

#         if dist[here] < cost:
#             continue

#         for next_node, next_cost in graph[here]:
#             if dist[next_node] > cost + next_cost:
#                 dist[next_node] = cost + next_cost
#                 heapq.heappush(q, (cost + next_cost, next_node))
#     return dist[a], dist[b]

# def solution(n, s, a, b, fares):
#     answer = 0
#     graph = [[] for _ in range(n + 1)]             # [linked node, cost]
    
#     for fare in fares:
#         start, end, cost = fare
#         graph[start].append((end, cost))            
#         graph[end].append((start, cost))
    
#     dist = [float('inf')] * (n + 1)
#     dist[s] = 0
#     visited = [False] * (n + 1)
#     minC = float('inf')
#     total = 0                                       # 함께 택시를 탔을 때의 비용
#     for _ in range(n):
#         minI = 0
#         minV = float('inf')

#         for i in range(1, n + 1):
#             if not visited[i] and minV > dist[i]:
#                 minV = dist[i]
#                 minI = i

#         # 현재 지점 방문
#         visited[minI] = True
#         total += minV
        
#         # 현재 지점에서 각자 택시를 타고 가는 경우
#         toA, toB = dijkstra(graph, minI, a, b, n)
#         minC= min(minC, total + toA + toB)

#         for next_node, next_cost in graph[minI]:
#             if dist[next_node] > next_cost:
#                 dist[next_node] = next_cost

#     print(minC)
#     return answer

# solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])

