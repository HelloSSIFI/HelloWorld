"""
Fail
"""
import sys
input = sys.stdin.readline

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

for k in range(1, N):
    for r in range(N):
        print(dp[r][:])
    print('='*100)
    for i in range(0, N-k):
        j = i + k
        dp[i][j] = 2**31
        dp[i][j] = min(dp[i][j],
                       # 좌측에서 계산
                       dp[i][j-1] + m[i][0] * m[j][0] * m[j][1],
                       # 하측에서 계산
                       dp[i+1][j] + m[i][0] * m[i][1] * m[j][1])

print(dp[0][-1])