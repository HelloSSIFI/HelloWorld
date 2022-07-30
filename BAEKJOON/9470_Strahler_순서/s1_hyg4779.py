from collections import deque
import sys
input = sys.stdin.readline
for tc in range(int(input())):
    K, M, P = map(int, input().split())

    graph = [[] for _ in range(M+1)]
    degree = [0]*(M+1)

    for _ in range(P):
        a, b = map(int, input().split())
        graph[a].append(b)
        degree[b] += 1
    Q = deque([n for n in range(1, M+1) if degree[n]==0])

    # 강 별 최대 순서와 들어온 줄기 수
    strahler = [[0, 0] for _ in range(M+1)]
    for i in range(1, M):
        if degree[i]==0:
            strahler[i][0] = 1

    while Q:
        now = Q.popleft()
        val = strahler[now][0]
        for node in graph[now]:
            # 현재 강이 갈 수 있는 노드를 탐색하며
            # 들어온 순서의 최대 크기와 들어온 강 줄기 수 갱신
            if strahler[node][0] < val:
                strahler[node] = [val, 1]
            elif strahler[node][0] == val:
                strahler[node][1] += 1

            degree[node] -= 1
            # 진입 차수가 끝난 노드
            if degree[node] == 0:
                # 진입이 끝나면 강 줄기도 더 이상 갱신 안됨
                if strahler[node][1] > 1:
                    strahler[node][0] += 1
                    strahler[node][1] = 0
                Q.append(node)

    print(f'{tc+1} {strahler[M][0]}')