import heapq


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    
    for edge_info in edge:
        a = edge_info[0]
        b = edge_info[1]

        graph[a].append(b)
        graph[b].append(a)


    q = []
    distances = [float('INF')] * (n + 1)
    distances[1] = 0
    heapq.heappush(q, (0, 1))

    while q:
        distance, node = heapq.heappop(q)
        
        if distances[node] < distance:
            return

        for next_node in graph[node]:
            next_distance = distances[node] + 1
            if distances[next_node] > next_distance:
                distances[next_node] = next_distance
                heapq.heappush(q, (next_distance, next_node))     

    distances = distances[1:]
    answer = distances.count(max(distances))
    return answer


'''
시간초과 fail

def dijkstra(graph, n):
    key = [float('INF')] * (n + 1)
    visited = [0] * (n + 1)
    key[1] = 0

    for _ in range(n):
        min_idx = 1
        min_value = float('INF')

        for i in range(1, n + 1):
            if not visited[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        
        visited[min_idx] = 1

        for node in graph[min_idx]:
            distance = key[min_idx] + 1
            if key[node] > distance:
                key[node] = distance

    return key




def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    
    for edge_info in edge:
        a = edge_info[0]
        b = edge_info[1]

        graph[a].append(b)
        graph[b].append(a)

    distances = dijkstra(graph, n)[1:]
    answer = distances.count(max(distances))
    return answer
'''

'''
다른 사람의 풀이1
일반 q를 이용한 풀이(BFS)

def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    distances = [ 0 for _ in range(n) ]
    is_visit = [False for _ in range(n)]
    queue = [0]
    is_visit[0] = True
    for (a, b) in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer

'''
'''
다른 사람의 풀이2 (BFS)
유사딕셔너리 defaultdict로 편리하게 그래프 형성이 가능

from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]
    visited = set([start])

    while len(q) > 0:
        current = q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1

def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)

    max_distance = max(distances)
    answer = 0

    for distance in distances:
        if distance == max_distance:
            answer += 1

    return answer
'''



solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])