def solution(triangle):
    N = len(triangle)
    dp = [[0]*n for n in range(1, N+1)]
    dp[N-1] = triangle[N-1][:]

    for i in range(N-2, -1, -1):
        for j in range(len(dp[i])):
            dp[i][j] = max(dp[i][j], triangle[i][j] + dp[i+1][j], triangle[i][j] + dp[i+1][j+1])

    return dp[0][0]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))