import sys
input = sys.stdin.readline

N = int(input())

game = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        elif dp[i][j]:
            if i + game[i][j] < N:
                dp[i + game[i][j]][j] += dp[i][j]

            if j + game[i][j] < N:
                dp[i][j + game[i][j]] += dp[i][j]

print(dp[N-1][N-1])
