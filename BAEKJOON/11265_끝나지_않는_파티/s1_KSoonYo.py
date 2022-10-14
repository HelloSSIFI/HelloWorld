# 모든 노드 대 모든 노드 간 최단 거리 : 플로이드 워셜 알고리즘 O(n^3)

import sys
input = sys.stdin.readline

def Floyd_warshall(N, MAP):
    for node in range(N):
        for i in range(N):
            for j in range(N):
                if MAP[i][j] > MAP[i][node] + MAP[node][j]:
                    # i에서 j까지 가는 길 거리가 node를 거쳐서 지나갈 때보다 큰 경우 -> 거리 갱신
                    MAP[i][j] = MAP[i][node] + MAP[node][j]

    return

N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]

Floyd_warshall(N, MAP)

for _ in range(M):
    s, e, c = map(int,input().split())
    if MAP[s-1][e-1] > c:
        print('Stay here')
    else:
        print('Enjoy other party')



# 노드 대 모든 노드 간 최단 거리 : 다익스트라 -> 시간 초과


# def routing(N, MAP, s, e):
#     dist = [float('INF')] * N
#     dist[s-1] = 0
#     q = [(0, s-1)]                        # (소요 시간, 노드 번호)
#     while q:
#         cost, node = heapq.heappop(q)
        
#         if dist[node] < cost:
#             continue

#         for next_node in range(N):
#             if MAP[node][next_node] and dist[next_node] > cost + MAP[node][next_node]:
#                 dist[next_node] = cost + MAP[node][next_node]
#                 heapq.heappush(q, (cost + MAP[node][next_node], next_node))

#     return dist[e-1]

# N, M = map(int, input().split())
# MAP = [list(map(int, input().split())) for _ in range(N)]
# for _ in range(M):
#     s, e, c = map(int,input().split())
#     T = routing(N, MAP, s, e)
#     if c < T:
#         print('Stay here')
#     else:
#         print('Enjoy other party')

