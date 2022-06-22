N, K = map(int, input().split())
coins = {int(input()) for _ in range(N)}
dp = [0] + [K + 1] * K

for coin in coins:                          # 현재 동전을 썼을때와 안썼을 때 동전의 개수를 비교하여
    for i in range(K - coin + 1):           # 적은 쪽으로 dp에 저장
        dp[coin + i] = min(dp[coin + i], dp[i] + 1)

if dp[-1] == K + 1:             # 반복이 끝나도 dp가 그대로이면
    dp[-1] = -1                 # 만들수 없는 금액이므로 -1

print(dp[-1])
