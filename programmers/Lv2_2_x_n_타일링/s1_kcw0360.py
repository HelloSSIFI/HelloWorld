def solution(n):
    dp = [0, 1, 2]   # 2 x n 타일을 채울 때 n이 0, 1, 2일 때 나올 수 있는 경우의 수

    if n > 2:    # n이 3보다 큰 경우 진행
        dp += [0] * (n - 2)
        for i in range(3, n+1):    # n까지
            dp[i] = (dp[i-1] + dp[i-2]) % 1000000007    # 피보나치 수열과 같은 규칙, 조건에 있는 값을 나눠 준다

    return dp[n]