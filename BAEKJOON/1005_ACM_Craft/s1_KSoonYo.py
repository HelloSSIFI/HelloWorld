# 백준 2252 줄 세우기 문제와 유사(위상정렬)
# A - B 순서대로 건물을 지을 때, B를 짓고 다시 A를 지을 일은 없으므로 사이클이 존재하지 않음

import sys
from collections import deque

input = sys.stdin.readline
        
for _ in range(int(input())):
    N, K = map(int, input().split())                    # N : 건물의 개수, K : 건설 순서 규칙
    costs = [0] + list(map(int, input().split()))       # 건물을 지을 때 걸리는 시간
    build = [[] for _ in range(N + 1)]                  # 건물 짓는 순서 그래프
    degree = [0] * (N + 1)                              # 진입 차수 기록
    dp = [0] * (N + 1)                                  # 1~N 중 현재 인덱스 번호의 건물까지 도달하는데 걸리는 시간 중 최적의 시간 기록

    for i in range(K):                                  # 건물 순서 그래프와 진입 차수 입력받기
        start, end = map(int, input().split())          
        build[start].append(end)
        degree[end] += 1

    W = int(input())                                    # 목표 건물 번호
    q = deque()                                         

    for idx in range(1, N + 1):                         # 처음 지을 건물 번호 추출
        if degree[idx] == 0:                            # 진입 차수가 0인 것 뽑기
            dp[idx] = costs[idx]
            q.append(idx)

    while q:                                            # 위상정렬 알고리즘 
        now = q.popleft()
        if now == W:                                    # 목표 건물에 도달했다면 break
            print(dp[W])
            break

        for next in build[now]:
            degree[next] -= 1                               # 다음에 진입하는 건물의 진입 차수에서 현재 건물과 이어진 간선 끊기
            dp[next] = max(dp[next], costs[next] + dp[now]) # dp 갱신(기존에 기록했던 시간과 새로 진입하는 시간 중 큰 것을 기록) 
            if degree[next] == 0:                           # 다음 건물 번호의 진입 차수가 0이 되었다면 다음에 방문할 노드로 q에 추가
                q.append(next)
    
