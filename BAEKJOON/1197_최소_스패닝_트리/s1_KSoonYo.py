# 프림 알고리즘을 이용한 최소 신장 트리 -> 메모리 초과
# v가 10000인 관계로 인접행렬로 풀긴 어렵다.
# heapq를 이용해서 prim알고리즘을 구현하거나
# 크루스칼 알고리즘으로 풀어야 함

def prim(start):
    key = [0] + [987654321] * V
    key[start] = 0
    visited = [0] * (V + 1)

    for _ in range(1, V + 1):
        u = start
        minV = float('INF')

        for idx in range(1, V + 1):
            if not visited[idx] and key[idx] < minV:
                u = idx
                minV = key[idx]
        visited[u] = 1

        for node_idx in range(1, V + 1):
            if graph[u][node_idx] and (not visited[node_idx]):
                if key[node_idx] > graph[u][node_idx]:
                    key[node_idx] = graph[u][node_idx]
                
    return sum(key)

V, E = map(int, input().split())                
 
graph = [[0] * (V + 1)  for _ in range(V + 1)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start][end] = graph[end][start] = weight


print(prim(1))

