import sys
from collections import deque
input = sys.stdin.readline


N, M, K = map(int, input().split())
graph = [list(input().strip()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
dist_map = [[float('inf')] * M for _ in range(N)]

dist_map[x1 - 1][y1 - 1] = 0

q = deque([(x1 - 1, y1 - 1)])                              # [dist, x좌표, y좌표]
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]                     # 상 하 좌 우
while q:
    r, c = q.popleft()

    for d in dirs:
        nr = r + d[0] 
        nc = c + d[1]
        nk = 1
        
        # while 문 조건 지정 주의: 방문 체크를 if 문으로 q append 조건의 형태로 지정하면 while문의 조건이 true가 될 때 불필요한 반복을 할 수 있다.(한쪽으로 갈 수 있는 길이 막히면 그 방향은 고려할 필요 x)  
        while 0 <= nr < N and 0 <= nc < M and graph[nr][nc] != '#' and nk <= K and dist_map[r][c] < dist_map[nr][nc]:     # 한 방향을 정했으면 최대 K칸까지 계속 이동!
            if dist_map[nr][nc] == float('inf'):
                dist_map[nr][nc] = dist_map[r][c] + 1
                q.append((nr, nc))
            
            nr += d[0]
            nc += d[1]
            nk += 1

if dist_map[x2 - 1][y2 - 1] != float('inf'):
    print(dist_map[x2 - 1][y2 - 1])
else:
    print(-1)

