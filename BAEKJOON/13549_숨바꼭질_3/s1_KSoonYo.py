# 0 1 bfs를 이용한 풀이
# 가중치가 0과 1인 너비 우선 탐색, 시간 복잡도 O(V + E)

from collections import deque

N, K = map(int, input().split())
q = deque([(0, N)])                                     # (소요된 시간, 현재 위치)
dist = [float('inf')] * (100001 * 2)
dist[N] = 0
while q:
    t, here = q.popleft()

    if here == K:
        print(t)
        break

    # 현재 위치와 인접한 노드( here - 1, here + 1, 2 * here )
    # 간선 가중치가 0이면 queue front, 1이면 back
    for cost, next in [(1, here - 1), (1, here + 1), (0, 2 * here)]:
        if next >= len(dist) or next < 0:
            continue
        
        if dist[next] > t + cost:
            dist[next] = t + cost
            if cost:
                q.append((t + cost, next))
            else:
                q.appendleft((t + cost, next))

