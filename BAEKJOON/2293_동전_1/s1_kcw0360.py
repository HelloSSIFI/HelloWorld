N, K = map(int, input().split())

coins = []    # 사용할 동전 종류
dp = [1] + [0] * K    # 경우의 수 체크

for _ in range(N):
    coins.append(int(input()))

for coin in coins:    # 해당 동전을 가지고 만들 수 있는 경우의 수 찾기
    for i in range(coin, K+1):    # i값을 만드는 데 있어서 coin 가치로 만들 수 있는 경우의 수는 i, i-coin가 같은 경우의 수를 가진다.
        dp[i] += dp[i-coin]

print(dp[K])