from collections import deque
import sys
input = sys.stdin.readline
'''
진입 차수를 따라 다음 타겟을 검색
다음 타겟으로 가는 경우를 모두 탐색하며 그 경우 중
가장 오래 걸리는(짧은 것들은 이전에 다 끝남) 경우로 DP테이블 갱신
최종 도달 지점의 DP 값 print
'''

for tc in range(int(input())):
    # 건물 개수,건설 순서 규칙 K 개
    N, K = map(int, input().split())

    #각 건물당 건설 시간 N 개
    constr = list(map(int, input().split()))

    graph = [[] for i in range(N)]

    # 진입차수
    degree = [0]*N
    for _ in range(K):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        degree[b-1] += 1

    win = int(input())-1            # 타겟

    DP = [0]*N
    Q = deque([])
    for i in range(N):
        # 진입 차수가 0이면 Q에 넣고 탐색
        if degree[i] == 0:
            Q.append(i)
            DP[i] += constr[i]

    while Q:
        now = Q.popleft()

        for j in graph[now]:
            # 해당 노드가 갈 수 있는 노드에서 진입 차수를 -1 해줌
            # 도달 하는 노드로 가는 경우 중 오래 걸리는 경우로 갱신해줌
            degree[j] -= 1
            DP[j] = max(DP[j], DP[now]+constr[j])

            if degree[j]==0:
                Q.append(j)


    print(DP[win])