from collections import deque

N, M = map(int, input().split())    # N: 세로, M: 가로
maze = [list(map(int, input())) for _ in range(n)]
visited = [[0]*M for _ in range(N)]


def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        a, b = q.popleft()

        if a == N-1 and b == M-1:
            break

        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]

            if 0 <= y < N and 0 <= x < M and maze[y][x] == 1 and visited[y][x] == 0:
                visited[y][x] = visited[a][b] + 1
                q.append([y, x])

                if [y, x] == [N-1, M-1]:
                    return visited[y][x]


print(bfs())

