import sys

N = int(sys.stdin.readline())
n_map = [list(sys.stdin.readline().rstrip()) for _ in range(N)]

visited = [[0] * N for _ in range(N)]
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # 상 우 하 좌
ans = []
cnt = 0


def bfs(y, x, v):
    global cnt
    cnt += 1
    visited[y][x] = v
    for (dy, dx) in di:
        next_x = x + dx
        next_y = y + dy
        if (0 <= next_x < N and 0 <= next_y < N) and n_map[next_y][next_x] == '1' and visited[next_y][next_x] == 0:
            bfs(next_y, next_x, v)


n_complex = 1
for i in range(N):
    for j in range(N):
        if n_map[i][j] == '1' and visited[i][j] == 0:
            bfs(i, j, n_complex)
            n_complex += 1
            ans.append(cnt)
            cnt = 0

ans.sort()
print(n_complex - 1)
print(*ans, sep='\n')