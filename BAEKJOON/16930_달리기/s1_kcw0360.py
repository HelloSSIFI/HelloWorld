from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
gym = [list(input()) for _ in range(N)]
x1, y1, x2, y2 = map(int, input().split())
visited = [[-1] * M for _ in range(N)]
q = deque()
q.append([x1-1, y1-1])
visited[x1-1][y1-1] = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

while q:
    a, b = q.popleft()

    if a == x2-1 and b == y2-1:
        break

    for k in range(4):
        for l in range(1, K+1):
            i = a + dy[k] * l
            j = b + dx[k] * l
            if 0 <= i < N and 0 <= j < M:
                if gym[i][j] == '#':
                    break

                if visited[i][j] == -1:
                    visited[i][j] = visited[a][b] + 1
                    q.append([i, j])
                elif visited[i][j] == visited[a][b]+1:
                    continue
                else:
                    break
            else:
                break

print(visited[x2-1][y2-1])