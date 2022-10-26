'''
import heapq
실패코드 다익스트라
def so(n, roads, sources, destination):
    answer = []
    MAX = 1000001
    graph = [[] for _ in range(n+1)]

    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)

    def dijstra(start):
        queue = []
        heapq.heappush(queue, (0, start))

        distance = [MAX]*(n+1)
        distance[start] = 0

        while queue:
            dist, now = heapq.heappop(queue)

            if distance[now] < dist:
                continue

            for i in graph[now]:
                cost = dist + 1
                if cost < distance[i]:
                    distance[i] = cost
                    heapq.heappush(queue, (cost, i))

        return distance[destination]

    for start in sources:
        res = dijstra(start)
        answer.append(-1 if res == MAX else res)

    return answer
'''

from collections import deque

def solution(n, roads, sources, destination):
    '''
    destination에서 출발하여
    도달할 수 있는 모든 노드의 최단시간을 저장하고 순서대로 return
    '''
    visit = [-1]*(n+1)
    graph = [[] for _ in range(n+1)]
    for s, e in roads:
        graph[s].append(e)
        graph[e].append(s)

    Q = deque([destination])
    visit[destination] = 0

    while Q:
        now = Q.popleft()

        for node in graph[now]:
            if visit[node] == -1:
                visit[node] = visit[now]+1
                Q.append(node)

    return [visit[i] for i in sources]

print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))