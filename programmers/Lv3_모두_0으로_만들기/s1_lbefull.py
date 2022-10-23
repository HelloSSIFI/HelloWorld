from collections import deque


def solution(a, edges):
    if sum(a): return - 1

    answer = 0
    N = len(a)
    lines = [set() for _ in range(N)]
    for u, v in edges:                              # 트리의 연결정보를 인접리스트 방식으로 저장
        lines[u].add(v)
        lines[v].add(u)

    Q = deque()
    for i in range(N):                              # 트리의 리프노드를 Q에 넣어줌
        if len(lines[i]) == 1: Q.append(i)

    while Q:
        v = Q.popleft()

        nextv = -1                                  # 방문하지 않았고 연결된 노드가 1개 또는 0개 뿐인 노드만 Q에 들어있음
        for i in lines[v]:                          # 따라서 nextv는 연결된 유일한 노드 또는 -1을 가리킴
            nextv = i

        if nextv == -1: continue                    # 연결된 노드가 없다면 다음반복

        a[nextv] += a[v]                            # 방문하지 않은 연결된 노드에 현재 노드의 숫자를 넘겨줌
        answer += abs(a[v])                         # 결과값에는 해당 수의 크기만큼 추가
        a[v] = 0                                    # 현재 노드는 0이 되고
        lines[nextv].discard(v)                     # 다음노드에 연결된 간선에서 현재 노드를 지워버림

        if len(lines[nextv]) > 1: continue          # 연결된 노드가 2개 이상이면 다음반복

        Q.append(nextv)                             # 아니라면 Q에 다음노드 추가

    return answer


print(solution([-5, 0, 2, 1, 2], [[0, 1], [3, 4], [2, 3], [0, 3]]))
