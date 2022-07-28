from collections import deque
import sys
input = sys.stdin.readline


for _ in range(int(input())):
    K, M, P = map(int, input().split())
    come = [[] for i in range(M + 1)]               # 인덱스 번호로 진입하는 노드를 저장
    go = [[] for i in range(M + 1)]                 # 인덱스 번호에서 갈 수 있는 노드를 저장
    visited = [0] * (M + 1)                         # 방문여부와 Strahler 순서를 저장
    Q = deque()

    for i in range(P):
        a, b = map(int, input().split())
        go[a].append(b)                             # 진출하는 노드와
        come[b].append(a)                           # 진입하는 노드를 각각 저장

    for i in range(1, M):
        if not come[i]:                             # 강이 시작되는 부분은
            visited[i] = 1                          # 순서를 1로 바꿔주고
            for g in go[i]:                         # 해당 노드에서 갈 수있는 곳을 Q에 enQ
                Q.append(g)
    
    while Q:                                        # Q가 빌 때 까지
        v = Q.popleft()

        max_order = 0
        cnt = 0
        for i in come[v]:                           # Q의 첫 번째 요소로 진입하는 노드 순회
            if not visited[i]:                      # 해당 노드들 중 방문한 적이 없는것이 있다면
                continue                            # 현재 노드는 무시하고 다음반복

            if visited[i] > max_order:              # 아니라면 진입하는 노드의 순서를 비교하여
                max_order = visited[i]              # 가장 큰 수와 개수를 구해줌
                cnt = 1
            elif visited[i] == max_order:
                cnt += 1
        
        visited[v] = max_order                      # 현재 노드를 가장 큰 수에 맞춰주고
        if cnt > 1:                                 # 그 수가 2개 이상이면 +1
            visited[v] += 1
        
        for i in go[v]:                             # 현재 노드에서 갈 수 있는 노드들을
            Q.append(i)                             # Q에 enQ
    
    print(f'{K} {visited[M]}')
