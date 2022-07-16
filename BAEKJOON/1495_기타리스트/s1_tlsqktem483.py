"""
다이나믹 프로그래밍
"""
import sys

N, S, M = map(int, sys.stdin.readline().split())
V = list(map(int, sys.stdin.readline().split()))

dp = [[0] * (M+1) for _ in range(N+1)]
dp[0][S] = 1

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] != 0:
            if j + V[i-1] <= M:
                dp[i][j + V[i-1]] = 1
            if 0 <= j - V[i-1]:
                dp[i][j - V[i-1]] = 1

ans = -1

for j in range(M, -1, -1):
    if dp[N][j] == 1:
        ans = j
        break

print(ans)