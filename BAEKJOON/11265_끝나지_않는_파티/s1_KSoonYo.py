# 모든 노드 대 모든 노드 간 최단 거리 : 플로이드 워셜 알고리즘 O(n^3)

import sys
import heapq

input = sys.stdin.readline

# def Floyd_warshall(N, MAP):
#     for node in range(N):
#         for i in range(N):
#             for j in range(N):
#                 if MAP[i][j] > MAP[i][node] + MAP[node][j]:
#                     # i에서 j까지 가는 길 거리가 node를 거쳐서 지나갈 때보다 큰 경우 -> 거리 갱신
#                     MAP[i][j] = MAP[i][node] + MAP[node][j]

#     return

# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]

# Floyd_warshall(N, MAP)

# for _ in range(M):
#     s, e, c = map(int,input().split())
#     if MAP[s-1][e-1] > c:
#         print('Stay here')
#     else:
#         print('Enjoy other party')



# 노드 대 모든 노드 간 최단 거리 : 다익스트라 -> 시간 초과

def routing(N, MAP, s, e, t):
    
    q = []

    for node in range(N):
        if node != (s-1):
            heapq.heappush(q, (MAP[s-1][node], node))

    while q:
        cost, node = heapq.heappop(q)

        if cost > MAP[s-1][node]:
            continue

        for next_node in range(N):
            if node == next_node:
                continue
            if cost + MAP[node][next_node] < MAP[s-1][next_node]:
                MAP[s-1][next_node] = cost + MAP[node][next_node]
                heapq.heappush(q, (cost + MAP[node][next_node], next_node))
            if next_node == (e - 1) and MAP[s-1][next_node] <= t:
                return True

    return False


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    s, e, c = map(int,input().split())
    if routing(N, MAP, s, e, c):
        print('Enjoy other party')
    else:
        print('Stay here')

