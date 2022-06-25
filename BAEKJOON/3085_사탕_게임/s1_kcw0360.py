def candies(N):
    ans = 1

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if colors[i][j] == colors[i][j-1]:
                cnt += 1
            else:
                cnt = 1

            ans = max(ans, cnt)

    for i in range(N):
        cnt = 1
        for j in range(1, N):
            if colors[j][i] == colors[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            ans = max(ans, cnt)

    return ans


N = int(input())
colors = [list(input()) for _ in range(N)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

result = 0

for i in range(N):
    for j in range(N):
        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]

            if 0 <= y < N and 0 <= x < N and colors[i][j] != colors[y][x]:
                colors[i][j], colors[y][x] = colors[y][x], colors[i][j]
                result = max(result, candies(N))
                colors[i][j], colors[y][x] = colors[y][x], colors[i][j]

print(result)