from collections import deque
import sys
input = sys.stdin.readline


for tc in range(int(input())):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    go = [set() for _ in range(N)]                      # 진출 노드
    come = [set() for _ in range(N)]                    # 진입 노드
    visited = [0] * (N)
    for _ in range(K):
        x, y = map(int, input().split())
        go[x - 1].add(y - 1)
        come[y - 1].add(x - 1)
    W = int(input()) - 1

    Q = deque()
    for i in range(N):                                  # 시작 위치를 Q에 enQ
        if not come[i]:
            Q.append(i)
    
    while Q:
        v = Q.popleft()                                 # 확인할 노드를 Q에서 deQ

        visited[v] += D[v]                              # 현재 건물 시간을 추가해주고

        if v == W:                                      # 목표 건물이면 반복 종료
            break

        for e in go[v]:                                 # 현재 건물을 지어야만 지을 수 있는 건물들을 탐색
            visited[e] = max(visited[e], visited[v])    # 시간이 가장 큰 것을 선택
            come[e].remove(v)                           # 현재 건물과의 연결을 끊어주고
            if not come[e]:                             # 다음 건물에 진입하는 노드 더 이상 없다면
                Q.append(e)                             # Q에 넣어줌
    
    print(visited[W])
