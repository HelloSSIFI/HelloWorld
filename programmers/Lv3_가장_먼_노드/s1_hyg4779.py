from collections import deque


def solution(n, edge):
    edges = [[] for _ in range(n+1)]            # 간선들을 저장할 인접리스트
    for tmp in edge:                            # 간선 정보 저장
        a, b = tmp
        edges[a].append(b)
        edges[b].append(a)

    visit = [0]*(n+1)                           # 방문처리와 거리를 동시에 처리할 배열
    q = deque([1])                              # BFS를 구현할 큐


    while q:
        now = q.popleft()                       # 현재 위치와 이동한 거리

        for node in edges[now]:

            if node == 1:continue               # 1번 노드는 제외

            if not visit[node]:                 # 방문하지 않은 노드는 제외
                d = visit[now] + 1
                visit[node] = d
                q.append(node)




    # visit 배열에서 최댓값이 같은 값들의 개수를 반환하는 식
    return visit.count(max(visit))
    # return len(list(filter(lambda x: x==max(visit), visit)))