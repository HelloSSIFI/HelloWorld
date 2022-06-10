import sys
input = sys.stdin.readline

V, E = map(int, input().split())
lines = [[] for _ in range(V + 1)]
cost = [1000001] * (V + 1)                  # 비용 초기화
visited = [0] * (V + 1)

for _ in range(E):
    s, e, c = map(int, input().split())     # 인접 리스트 형식으로 간선 저장
    lines[s].append((e, c))                 # 양방향으로 저장
    lines[e].append((s, c))

cost[1] = 0                                 # 처음 시작 위치를 1번으로 설정

for _ in range(V):
    min_idx = 0
    min_value = 1000001
    for i in range(1, V + 1):                           # 발견된 정점 중 방문하지 않은 최소 비용을 찾음
        if not visited[i] and min_value > cost[i]:
            min_value = cost[i]
            min_idx = i
    
    visited[min_idx] = 1                                # 해당위치 방문표시

    for e, c in lines[min_idx]:                         # 해당위치에서 갈 수 있는 곳 탐색
        if not visited[e]:                              # 방문하지 않은 곳이면
            cost[e] = min(cost[e], c)                   # 비용을 비교 후 갱신

print(sum(cost) - 1000001)                              # 0번 노드는 없으므로 0번 노드 비용을 빼줌
