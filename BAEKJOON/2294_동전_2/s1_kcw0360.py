N, K = map(int, input().split())

coins = []
dp = [0] + [10001] * K

for _ in range(N):
    coins.append(int(input()))

for coin in coins:
    for i in range(coin, K+1):
        if dp[i] > 0:
            dp[i] = min(dp[i], dp[i-coin]+1)

if dp[K] == 10001:
    print(-1)
else:
    print(dp[K])