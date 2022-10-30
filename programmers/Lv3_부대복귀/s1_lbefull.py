from collections import deque


def solution(n, roads, sources, destination):
    answer = []
    lines = [[] for _ in range(n)]
    for a, b in roads:                              # 인접 리스트 형태로 길 정보 저장
        lines[a - 1].append(b - 1)
        lines[b - 1].append(a - 1)

    cost = [-1] * n                                 # 강철부대 지역에서 각 지역으로의 비용을 저장
    cost[destination - 1] = 0                       # 강철부대 지역은 이동 비용이 0
    Q = deque()
    Q.append(destination - 1)
    while Q:                                        # 이동 비용이 1로 같으므로 queue를 사용한 BFS 탐색
        v = Q.popleft()
        for nv in lines[v]:
            if cost[nv] == -1:                      # 방문하지 않은 지역을 현재지역 +1의 비용으로 저장
                cost[nv] = cost[v] + 1
                Q.append(nv)

    for source in sources:
        answer.append(cost[source - 1])

    return answer


# print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
