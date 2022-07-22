import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().split())    # N: 정점의 개수, M: 간선의 개수
S, T = 1, 2    # S: 시작점, T: 도착점
graph = [[] for _ in range(N+1)]
distance = [2147483647] * (N+1)    # 이동거리
dp = [0] * (N+1)    # 최단 경로
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

heap = [[0, T]]
distance[T] = 0
dp[T] = 1

while heap:
    dis, now = heapq.heappop(heap)    # 이동거리, 현재위치

    if dis > distance[now]:    # 이동거리가 저장된 이동거리보다 긴 경우
        continue

    for i, j in graph[now]:    # i:다음 정점, j:현 위치와 다음 정점 까지의 길이
        dist = j + dis    # 다음 정점 까지의 총 거리 = 다음 정점 까지의 길이 + 현재까지 이동거리

        if dist < distance[i]:    # 다음 정점 까지의 총 거리가 저장된 거리보다 짧다면 저장
            distance[i] = dist
            heapq.heappush(heap, [dist, i])

        if dis > distance[i]:    # 다음 정점까지 이동거리가 현재 이동거리보다 짧을 경우 합리적인 이동경로
            dp[now] += dp[i]

print(dp[S])