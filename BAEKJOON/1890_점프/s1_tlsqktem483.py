import sys

N = int(sys.stdin.readline())
game_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        now = game_map[i][j]
        if i == N - 1 and j == N - 1:
            print(dp[i][j])
            break

        if now + j < N:
            dp[i][j + now] += dp[i][j]
        if now + i < N:
            dp[i + now][j] += dp[i][j]