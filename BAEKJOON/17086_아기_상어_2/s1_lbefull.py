from collections import deque


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
Q = deque()
for r in range(N):
    for c in range(M):
        if arr[r][c]:                           # 상어 위치를 찾아 방문표시하고 Q에 넣어줌
            Q.append((r, c))
            visited[r][c] = 1

dr = [-1, -1, 0, 1, 1, 1, 0, -1]                # 8방향 탐색
dc = [0, 1, 1, 1, 0, -1, -1, -1]
result = 0

while Q:                                        # BFS 탐색
    r, c = Q.popleft()

    for d in range(8):                          # 방문하지 않은 곳이면
        nr = r + dr[d]                          # 현재 거리 + 1로 표시하고 Q에 넣어줌
        nc = c + dc[d]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            Q.append((nr, nc))
            visited[nr][nc] = visited[r][c] + 1
            result = visited[r][c]

print(result)
