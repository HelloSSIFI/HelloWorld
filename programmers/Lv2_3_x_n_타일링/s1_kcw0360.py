def solution(n):
    if n % 2:    # 가로가 홀수인 경우는 존재하지 않기 때문에 0
        return 0

    n //= 2    # 짝수만 체크
    dp = [0, 3, 11] + [0] * (n - 2)

    # 점화식(n이 홀수일 때 값이 0인 경우를 포함)
    # f(n) = 4*f(n-2) - f(n-4)
    for i in range(3, n + 1):
        dp[i] = (4 * dp[i - 1] - dp[i - 2]) % 1000000007

    return dp[n]