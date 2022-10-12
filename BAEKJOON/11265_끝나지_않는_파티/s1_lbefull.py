import sys, heapq
input = sys.stdin.readline


def dijk(s):
    cost = [500000001] * N
    cost[s] = 0
    heap = [[0, s]]
    visited = [0] * N

    while heap:
        c, idx = heapq.heappop(heap)
        if visited[idx]:
            continue

        visited[idx] = 1
        for i in range(N):
            if not visited[i] and c + lines[idx][i] < cost[i]:
                cost[i] = c + lines[idx][i]
                heapq.heappush(heap, [c + lines[idx][i], i])

    return cost


N, M = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]
costs = []
for i in range(N):
    costs.append(dijk(i))

answer = []
for i in range(M):
    A, B, C = map(int, input().split())
    if costs[A - 1][B - 1] > C:
        answer.append('Stay here\n')
    else:
        answer.append('Enjoy other party\n')

print(''.join(answer))
