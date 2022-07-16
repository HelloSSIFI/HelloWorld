import sys
n, s, m = map(int, input().split())

# 볼륨리스트 v, 현재볼륨 p
V = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(m+1) for _ in range(n+1)]

dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            if j+V[i] <= m:
                dp[i+1][j+V[i]] = 1
            if j-V[i] >= 0:
                dp[i+1][j-V[i]] = 1


ans = -1
for i in range(m, -1, -1):
    if dp[n][i]:
        ans = i
        break
print(ans)