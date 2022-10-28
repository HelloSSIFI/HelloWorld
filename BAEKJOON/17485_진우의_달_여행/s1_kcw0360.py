N, M = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(N)]
dp = [[[9876543210]*3 for _ in range(M)] for _ in range(N)]
answer = 9876543210

for i in range(N):
    if i:
        for j in range(M):
            if j == 0:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + roads[i][j]
                dp[i][j][1] = dp[i-1][j][0] + roads[i][j]
            elif j == M-1:
                dp[i][j][1] = dp[i-1][j][2] + roads[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + roads[i][j]
            else:
                dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2]) + roads[i][j]
                dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2]) + roads[i][j]
                dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1]) + roads[i][j]
    else:    # 첫번째 줄인 경우
        for j in range(M):
            for d in range(3):
                dp[i][j][d] = roads[i][j]

for j in range(M):
    answer = min(min(dp[N-1][j]), answer)

print(answer)