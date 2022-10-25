from collections import deque

def solution(a, edges):
    answer = 0
    n = len(a)
    graph = [[] for _ in range(n)]

    # 간성정보 입력
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 루트 노드부터 리프 노드까지 이동경로
    route = []

    visit = [0]*n
    visit[0] = 1
    Q = deque([0])
    # route 찾기
    while Q:
        now = Q.popleft()
        route.append(now)

        for j in graph[now]:
            if visit[j] == 0:
                visit[j] = 1
                Q.append(j)

    # 리프노드를 0으로 만들고 부모노드에 더해감
    # 최종적으로 부모노드에 도착
    visit = [0]*n
    for i in range(n-1, -1, -1):
        node = route[i]
        visit[node] = 1

        # 현재 노드가 0이 아니라면 탐색, 0이면 넘어감
        if a[node]:

            for v in graph[node]:
                if visit[v] == 0 and a[node]:
                    a[v] += a[node]
                    answer += abs(a[node])
                    a[node] = 0

    return answer if a[0] == 0 else -1
