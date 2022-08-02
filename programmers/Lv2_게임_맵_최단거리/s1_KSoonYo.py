from collections import deque

def solution(maps):
    answer = 0
    visited = [[0] * (len(maps[0]) + 1) for _ in range(len(maps) + 1)]
    n, m = (len(maps), len(maps[0]))
    q = deque([(1, 1)])
    visited[1][1] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]   # 상 하 좌 우

    while q:
        now = q.popleft()

        if now == (n, m):
            break

        for i in range(4):
            nx = now[0] + dx[i]
            ny = now[1] + dy[i]

            if 0 < nx <= n and 0 < ny <= m and maps[nx- 1][ny - 1]:
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[now[0]][now[1]] + 1
                    q.append((nx, ny))

    if visited[n][m]:
        answer = visited[n][m]
    else:
        answer = -1

    return answer

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))

