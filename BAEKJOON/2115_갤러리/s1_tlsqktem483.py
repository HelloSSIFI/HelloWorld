ans = 0
M, N = map(int, input().split())
graph = [list(input()) for _ in range(M)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
visited = [[[False]*N for _ in range(M)] for _ in range(4)]


def check(i, j):
    global ans

    # Pattern 0, 1
    if graph[i+1][j] == '.':
        # Pattern 0
        if graph[i][j-1] == 'X' and graph[i+1][j-1] == 'X' and not visited[0][i][j]:
            visited[0][i][j], visited[0][i+1][j] = True, True
            ans += 1
        # Pattern 1
        if graph[i][j + 1] == 'X' and graph[i + 1][j + 1] == 'X' and not visited[1][i][j]:
            visited[1][i][j], visited[1][i + 1][j] = True, True
            ans += 1

    # Pattern 2, 3
    if graph[i][j+1] == '.':
        # Pattern 2
        if graph[i-1][j] == 'X' and graph[i - 1][j + 1] == 'X' and not visited[2][i][j]:
            visited[2][i][j], visited[2][i][j+1] = True, True
            ans += 1
        # Pattern 3
        if graph[i + 1][j] == 'X' and graph[i + 1][j + 1] == 'X' and not visited[3][i][j]:
            visited[3][i][j], visited[3][i][j + 1] = True, True
            ans += 1


for r in range(1, M-1):
    for c in range(1, N-1):
        if graph[r][c] == '.':
            check(r, c)

print(ans)