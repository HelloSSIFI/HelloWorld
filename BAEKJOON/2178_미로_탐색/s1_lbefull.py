from collections import deque

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
Q = deque()
Q.append((0, 0))
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while Q:                        # BFS 탐색
    r, c = Q.popleft()

    for d in range(4):          # 4방향 반복
        nr = r + dr[d]          # 방문하지 않은 길이면
        nc = c + dc[d]          # 이동 거리 누적하여 반복

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] == '1':
            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))
    
print(visited[-1][-1])
