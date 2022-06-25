N, K = map(int, input().split())        # N가지 동전, 목표 15원
coins = list({int(input()) for _ in range(N)})

memo = [K+1]*(K+1)                      # memoization 배열 (K+1은 만들지 못할 때 임의의 큰 수를 담은 것)
memo[0] = 0                             # 0원은 만들 수 없으니 0

for coin in coins:                      # 동전 탐색
    for i in range(coin, K+1):          # 배열 탐색
        if memo[i-coin] != K+1:         # 현재 값-동전의 배열 값이 있으면 갱신
            memo[i] = min(memo[i], memo[i-coin]+1)

print(memo[K] if memo[K]!=K+1 else -1)
