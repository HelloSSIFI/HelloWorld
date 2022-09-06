import heapq

def search(graph, n, gates, summits):
    intensity = [float('inf')] * (n + 1)
    q = []
    
    # 첫 출발 지점: 모든 출입구
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(q, gate)

    while q:
        s = heapq.heappop(q)

        if s in summits:
            continue
        
        for next, weight in graph[s]:
            # 다음 노드에 기록된 가중치가 현재 노드에서 진입할 경우의 intensity보다 클 경우
            # 모든 경로에 대해 최소 intensity를 구해야 하므로 최소값 갱신
            if intensity[next] > max(intensity[s], weight):     # max(현재 경로에서 지금까지의 최대 가중치, 현재 노드에서 다음 노드로 갈 때 가중치)
                intensity[next] = max(intensity[s], weight)
                heapq.heappush(q, next)

    result_1 = n + 1
    result_2 = float('inf')
    for summit in summits:
        if intensity[summit] < result_2:
            result_1 = summit
            result_2 = intensity[summit]
        elif intensity[summit] == result_2 and result_1 > summit:
            result_1 = summit

    return [result_1, result_2]
        


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n + 1)]
    
    for path in paths:
        s, e, w = path
        graph[s].append((e, w))
        graph[e].append((s, w))

    # summits를 리스트로 in 확인 시, 시간초과 -> set으로 변경
    answer = search(graph, n, gates, set(summits))
    return answer

solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])
solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
