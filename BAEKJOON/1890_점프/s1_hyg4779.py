import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[N-1][N-1])
            break

        zump = arr[i][j]

        if i+zump < N:
            dp[i+zump][j] += dp[i][j]
        if j+zump < N:
            dp[i][j+zump] += dp[i][j]