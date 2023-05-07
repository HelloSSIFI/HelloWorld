def solution(n):
    dp = [0, 1, 3, 10, 23]
    check = [8, 0, 2]
    if n > 4:
        dp += [0] * (n-4)
        for i in range(5, n+1):
            temp = i % 3
            dp[i] = (check[temp] + dp[i-1] + dp[i-2] * 2 + dp[i-3] * 5 + (2 if temp else 4)) % 1000000007
            check[temp] += (dp[i-1] * 2 + dp[i-2] * 2 + dp[i-3] * 4)
            check[temp] %= 1000000007

    return dp[n]