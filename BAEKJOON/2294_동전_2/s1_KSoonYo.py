import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()                                   # 중복을 제거하기 위한 동전 set
dp = [float('INF')] * (k + 1)                   # 초기 dp 테이블 설정
dp[0] = 0                                       # index는 임의의 k원, value는 해당 k원에 사용되는 동전의 최소 개수

for _ in range(n):
    coins.add(int(input()))

for i in range(1, k + 1):                       # 1원을 만들 때 동전 최소 개수, 2원을 만들 때 ... k원까지 진행
    if i in coins:                              # 임의의 k원짜리 동전이 있으면 그 동전 1개 사용
        dp[i] = 1
        continue

    for coin in coins:                          # 동전 순회
        if i < coin or dp[i - coin] < 0:        # i가 동전 가치보다 낮거나 dp[i - coin]이 -1이면 다음 동전으로 최소 개수 체크
            continue                             
        else:                                   # 점화식: f(k) = f(k-a) + f(a) # (k-a) >= 0 , f(a) = 1
            dp[i] = min(dp[i], dp[i - coin] + dp[coin]) 
            
    if dp[i] == float('inf'):                   # 모든 동전을 순회 후에도 dp[i]가 변화가 없다면
        dp[i] = -1                              # 해당 i원은 주어진 동전으로 만들 수 없으므로 -1

print(dp[k])
