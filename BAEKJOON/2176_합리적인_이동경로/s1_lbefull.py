import heapq, sys
input = sys.stdin.readline

N, M = map(int, input().split())
lines = [[] for _ in range(N + 1)]                  # 인접 리스트 방식
for _ in range(M):                                  # 양방향 간선 정보 저장
    s, e, c = map(int, input().split())
    lines[s].append((e, c))
    lines[e].append((s, c))

cost = [100000000] * (N + 1)                        # 2번 노드에서 최단 거리를 저장할 리스트
heap = [(0, 2)]
visited = [0] * (N + 1)                             # 합리적인 이동경로의 경우의 수를 저장할 리스트
visited[2] = 1

while heap:                                         # 다익스트라 알고리즘
    c, v = heapq.heappop(heap)                      # 발견한 간선 중 최단거리와 노드를 가져옴
    if cost[v] < 100000000:                         # 이미 방문한 노드이면
        continue                                    # 다음 반복

    cost[v] = c                                     # 아니라면 거리 갱신

    for e, l in lines[v]:                           # 해당 노드에서 갈 수 있는 노드를 탐색
        if cost[v] > cost[e]:                       # 이미 발견한 노드들 중 현재 노드로 방문하는 비용이 커진다면
            visited[v] += visited[e]                # 그 노드에서 경우의 수를 가져와서 누적해줌
        if cost[e] == 100000000:                    # 아직 발견하지 않은 노드라면
            heapq.heappush(heap, (c + l, e))        # heap에 거리와 노드를 넣어줌

print(visited[1])
