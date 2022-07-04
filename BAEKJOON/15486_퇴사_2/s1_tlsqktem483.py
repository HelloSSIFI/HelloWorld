import sys

n = int(sys.stdin.readline())
work = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [0] * (n+1)

m = 0
for i in range(n):
    m = max(m, dp[i])
    if i+work[i][0] > n:
        continue
    dp[i + work[i][0]] = max(m + work[i][1], dp[i + work[i][0]])

print(max(dp))