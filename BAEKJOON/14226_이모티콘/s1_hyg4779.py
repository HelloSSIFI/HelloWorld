S = int(input())

# 해당 이모티콘 개수 별 최소 시간을 담는 배열
dp = list(range(1003))
for i in range(2, 1001):
    j = 2
    while i*j <= 1002:
        dp[i*j] = min(dp[i*j], dp[i]+j)
        dp[i*j-1] = min(dp[i*j-1], dp[i*j]+1)
        j += 1

print(dp[S])