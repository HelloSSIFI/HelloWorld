import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]                        # 인접리스트 방식 저장
cost = [100000000] * (N + 1)                            # 비용 초기화
visited = [0] * (N + 1)

for i in range(M):
    s, e, c = map(int, input().split())
    adj[s].append((e, c))                               # 인접리스트에 도착지와 비용을 저장

start, goal = map(int, input().split())
cost[start] = 0                                         # 시작점 비용은 0

for _ in range(N):                                      # 다익스트라 방식
    min_idx = 0
    min_value = 100000000
    for i in range(1, N + 1):                           # 현재 발견된 곳 중 방문하지 않았고 최소비용으로 갈 수 있는 곳을 탐색
        if not visited[i] and min_value > cost[i]:
            min_idx = i
            min_value = cost[i]
    
    visited[min_idx] = 1                                # 찾은 위치를 방문 처리

    for e, c in adj[min_idx]:                           # 해당 위치에서 인접한 노드 탐색
        if not visited[e]:                              # 방문하지 않은곳이면
            cost[e] = min(cost[min_idx] + c, cost[e])   # 현 위치에서 이동할 경우 비용이 더 싸다면 갱신
    
print(cost[goal])
