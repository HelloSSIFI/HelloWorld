"""
다이나믹 프로그래밍
"""
import sys

N = int(sys.stdin.readline())
dp = [i for i in range(N+1)]

if len(dp) >= 6:
    for i in range(6, N+1):
        dp[i] = max([dp[i], dp[i-3]*2, dp[i-4]*3, dp[i-5]*4])

print(dp[-1])