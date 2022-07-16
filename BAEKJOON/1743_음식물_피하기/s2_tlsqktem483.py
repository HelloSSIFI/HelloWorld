"""
BFS
"""
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 상 우 하 좌
ans = 0

way_map = [["."]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    way_map[r-1][c-1] = "#"


queue = []
def bfs(i, j):
    global cnt
    queue.append((i, j))

    visited[i][j] = True
    cnt += 1

    while queue:
        (r, c) = queue.pop(0)

        for d in di:
            next_r, next_c = r + d[0], c + d[1]

            if 0 <= next_r < N and 0 <= next_c < M and not visited[next_r][next_c] and way_map[next_r][next_c] == "#":
                queue.append((next_r, next_c))
                visited[next_r][next_c] = True
                cnt += 1


cnt = 0
for i in range(N):
    for j in range(M):
        if way_map[i][j] == "#":
            bfs(i, j)
            ans = max(ans, cnt)
            cnt = 0

print(ans)
