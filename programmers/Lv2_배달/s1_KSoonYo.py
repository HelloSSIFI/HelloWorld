
# 다익스트라 활용
def check(graph, dist_map, visited, e, K):
    N = len(dist_map) - 1
    for _ in range(1, N + 1):
        minV = float('INF')
        idx = 0
        for i in range(1, N + 1):
            if not visited[i] and dist_map[i] < minV:
                minV = dist_map[i]
                idx = i
        visited[idx] = True
        for v in graph[idx]:
            next, weight = v
            if dist_map[next] > minV + weight:
                dist_map[next] = minV + weight
        
        if visited[e]:
            break
    
    if dist_map[e] <= K:
        return True
    return False




def solution(N, road, K):
    answer = 0
    graph = [[] for _ in range(N + 1)]

    for info in road:
        s, e, w = info[0], info[1], info[2]
        graph[s].append((e, w))
        graph[e].append((s, w))

    dist_map = [float('INF')] * (N + 1)
    visited = [False] * (N + 1)
    dist_map[1] = 0

    for e in range(1, N + 1):
        if check(graph, dist_map, visited, e, K):
            answer += 1
    
    return answer


solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)
# solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)