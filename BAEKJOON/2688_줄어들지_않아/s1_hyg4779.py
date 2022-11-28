# https://velog.io/@xx0hn/BOJ-Python-2688-줄어들지-않아

for _ in range(int(input())):
    n = int(input())
    dp = [[0]*10 for _ in range(n+1)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(10):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(sum(dp[n]))