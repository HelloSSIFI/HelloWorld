"""
DP
1000000007 의 나머지로 변환해야 시간초과 방지
"""
def solution(N):
    dp = [0] * (N+1)
    dp[1], dp[2] = 1, 2

    for n in range(3, N + 1):
        dp[n] = (dp[n-2] + dp[n-1]) % 1000000007

    return dp[-1]


print(solution(4))