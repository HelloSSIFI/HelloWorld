one = input()
two = input()

n, m = len(one), len(two)
dp = [[0]*(m+1) for _ in range(n+1)]

answer = 0

for i in range(1, n+1):
    for j in range(1, m+1):
        if one[i-1]==two[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

print(dp[-1][-1])