import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


# 현재위치에서 다음위치로 가는 가지 수와 거리를 더해나감
dp = [0 for _ in range(N+1)]
distance = [float('inf') for _ in range(N+1)]

# 2의 시작 비용 0
distance[2] = 0
# 2로 이동할 수 있는 방법 처음에 1
dp[2] = 1

# 2부터 시작
heap = [[0, 2]]
while heap:
    # 현재까지 비용, 현재 노드
    dist, now = heapq.heappop(heap)

    # 현재 비용이 이동할 수 있는 비용 보다 길면 제외
    if dist > distance[now]:continue

    for node, n_dist in graph[now]:
        # node까지 이동 비용 = 현재 to node 비용 + 현재 까지 비용
        cost = n_dist + dist

        # node까지 이동 비용이 현재 가능한 비용 보다 작으면
        if cost < distance[node]:
            # 갱신 및 힙에 추가
            distance[node] = cost
            heapq.heappush(heap, [cost, node])

        # 이미 node로의 비용이 현재 까지 거리보다 짧으면 합리적인 이동경로
        if dist > distance[node]:
            # 합리적인 이동경로 +1
            dp[now] += dp[node]

print(dp[1])