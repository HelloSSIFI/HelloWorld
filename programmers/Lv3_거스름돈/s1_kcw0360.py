def solution(n, money):
    dp = [1] + [0] * n

    for coin in money:    # 돈의 종류 순서대로 탐색
        for i in range(coin, n+1):    # coin(돈의 종류)으로 i원을 만들수 있는 방법은 i-coin 금액에 해당하는 방법의 수와 같다.
            dp[i] += dp[i-coin]

    return dp[n]