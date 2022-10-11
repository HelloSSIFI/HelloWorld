"""
IDEA : DP
"""
C, N = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
info.sort(key=lambda x: x[1])
end_point = C + info[-1][1]
dp = [float('inf')]*(end_point)
dp[0] = 0

for i in range(1, end_point):
    for cost, get in info:
        if i - get < 0 or dp[i-get] == float('inf'):
            continue

        dp[i] = min(dp[i], dp[i-get]+cost)

print(min(dp[C:]))