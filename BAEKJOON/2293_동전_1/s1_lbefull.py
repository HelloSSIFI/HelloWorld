N, K = map(int, input().split())
dp = [0] * (K + 1)
dp[0] = 1
for _ in range(N):
    coin = int(input())
    for j in range(coin, K + 1):            # 현재 동전을 포함해서 K 값을 만드려면
        dp[j] = dp[j] + dp[j - coin]        # 현재 동전을 사용하지 않고 K를 만든 경우 + 현재 동전을 무조건 사용해서 K를 만든 경우

print(dp[-1])
