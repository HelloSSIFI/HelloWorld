import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [input() for _ in range(N)]
visited = [[2000000] * M for _ in range(N)]
q = deque()
x1, y1, x2, y2 = map(int, input().split())
visited[x1 - 1][y1 - 1] = 0
q.append((x1 - 1, y1 - 1))

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

while q:                                        # BFS 탐색
    r, c = q.popleft()

    for d in range(4):                          # 4방향 K거리 탐색
        for l in range(1, K + 1):               # 한 방향으로 가다가 벽을 만나거나 이전 방문했던 곳 중 시간이 짧은 곳을 만나면
            nr = r + dr[d] * l                  # 다음반복
            nc = c + dc[d] * l                  # 길이고 처음가는 곳이면 방문표시 후 q에 넣어줌

            if 0 <= nr < N and 0 <= nc < M and (arr[nr][nc] == '#' or visited[nr][nc] <= visited[r][c]):
                break

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 2000000 and arr[nr][nc] == '.':
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))

if visited[x2 - 1][y2 - 1] == 2000000:
    visited[x2 - 1][y2 - 1] = -1

print(visited[x2 - 1][y2 - 1])
