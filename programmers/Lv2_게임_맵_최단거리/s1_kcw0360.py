def bfs(maze, n, m):
    visited = [[0] * m for _ in range(n)]
    q = []
    q.append([0, 0])
    visited[0][0] = 1

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    while q:
        st = q.pop(0)
        for k in range(4):
            i, j = st[0] + dy[k], st[1] + dx[k]

            if 0 <= i <= n - 1 and 0 <= j <= m - 1 and maze[i][j] != 0 and visited[i][j] == 0:
                q.append([i, j])
                visited[i][j] = visited[st[0]][st[1]] + 1

                if [i, j] == [n - 1, m - 1]:
                    return visited[i][j]

    return -1


def solution(maze):
    n = len(maze)
    m = len(maze[0])

    answer = bfs(maze, n, m)

    return answer