from collections import deque

def solution(n, paths, gates, summits):

    graph = [[] for _ in range(n+1)]
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])


    dist = [10000001 for _ in range(n+1)]
    for gate in gates:
        dist[gate] = 0

    Q = deque(gates)
    while Q:
        now = Q.popleft()
        if now in summits: continue
        for node, cost in graph[now]:
            cost = max(dist[now], cost)
            if dist[node] > cost:
                Q.append(node)
                dist[node] = cost


    min_dis = float('inf')
    min_summit = -1

    for summit in summits:
        if min_dis > dist[summit]:
            min_dis = dist[summit]
            min_summit = summit
        elif min_dis == dist[summit] and min_summit > summit:
            min_summit = summit

    return [min_summit, min_dis]

'''
import collections

def bfs(n, graph, gates, summits, distance):
    que = collections.deque(gates)
    while que:
        cur_loc = que.popleft()
        if cur_loc in summits: continue
        for next_loc, way in graph[cur_loc]:
            if distance[next_loc] > max(distance[cur_loc], way):
                que.append(next_loc)
                distance[next_loc] = max(distance[cur_loc], way)
                
    return distance
        
def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for a, b, c in paths:
        graph[a].append([b, c])
        graph[b].append([a, c])
        
    summits_dict = {}
    min_dis = float('inf')
    min_summit = -1
    for summit in summits:
        summits_dict[summit] = 1
    
    distance = [10000001 for _ in range(n+1)]
    for gate in gates:
        distance[gate] = 0
        
    distance = bfs(n, graph, gates, summits_dict, distance)
        
    for summit in summits:
        if min_dis > distance[summit]:
            min_dis = distance[summit]
            min_summit = summit
        elif min_dis == distance[summit] and min_summit > summit:
            min_summit = summit
                
    return [min_summit, min_dis]
'''