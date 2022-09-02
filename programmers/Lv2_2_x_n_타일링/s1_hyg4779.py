def solution(n):
    dp = [0]*(n)
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = (dp[i-1]+dp[i-2])%1000000007

    return dp[-1]

print(solution(4))