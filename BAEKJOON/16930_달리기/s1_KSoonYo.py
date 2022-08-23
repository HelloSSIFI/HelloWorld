import sys
from collections import deque
input = sys.stdin.readline

# dfs 같은 bfs 문제

N, M, K = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
dist_map = [[float('inf')] * M for _ in range(N)]

dist_map[x1 - 1][y1 - 1] = 0

q = deque([(0, x1 - 1, y1 - 1)])                              # (dist, x좌표, y좌표)
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]                     # 상 하 좌 우
while q:
    dist, r, c = q.popleft()

    for d in dirs:
        nr = r + d[0] 
        nc = c + d[1]
        nk = 1
        
        # while 문 조건 지정 주의: 방문 체크를 if 문으로 q append 조건의 형태로 지정하면 while문의 조건이 true가 될 때 불필요한 반복을 할 수 있다.(한쪽으로 갈 수 있는 길이 막히면 그 방향은 고려할 필요 x)  
        # 방문체크 시 주의: 이미 방문했던 곳이라도 이전 방향과 다른 방향으로도 k칸 만큼 확장을 해야 하므로
        # 방문 체크 조건은 (현재 dist + 1) < (이미 기록된 dist) 가 아닌 (현재 dist) < (이미 기록된 dist) 
        while 0 <= nr < N and 0 <= nc < M and graph[nr][nc] != '#' and nk <= K and dist < dist_map[nr][nc]:     # 한 방향을 정했으면 최대 K칸까지 계속 이동!
            if dist_map[nr][nc] == float('inf'):                                                                # 어차피 목적지에 도달한 순간 INF는 다른 값으로 갱신되었을 것
                dist_map[nr][nc] = dist + 1
                q.append((dist + 1, nr, nc))
            
            nr += d[0]
            nc += d[1]
            nk += 1

if dist_map[x2 - 1][y2 - 1] != float('inf'):
    print(dist_map[x2 - 1][y2 - 1])
else:
    print(-1)

