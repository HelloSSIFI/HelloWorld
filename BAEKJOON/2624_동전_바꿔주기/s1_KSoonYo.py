
# dp
# dp[k][n] : 동전 k개 종류로 n원을 만들 수 있는 방법의 수
import sys

input = sys.stdin.readline

T = int(input())
k = int(input())
coin = [[0, 0]]
dp = [[0 for _ in range(T+1)] for _ in range(k + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    coin.append([x, y])

dp[0][0] = 1
for i in range(1, k + 1):                               
    val, cnt = coin[i]                                  # 금액, 동전 개수
    for j in range(T + 1):                              # 0원부터 T원까지
        dp[i][j] = dp[i-1][j]                           # 현재 j 금액에 대해 이전 단계에서 기록했던 값을 가져옴 
        for v in range(1, cnt + 1):                     # 1개부터 동전 개수까지 
            if j-v*val >= 0:                            
                dp[i][j] += dp[i - 1][j - v * val]      
            else:
                break

print(dp[k][T])


#### 시간초과

import sys
import copy

input = sys.stdin.readline

def dfs(coins_table, coins, i, target):
    global cnt

    if target == 0:
        cnt += 1
        return 
    
    new_coins_table = coins_table.copy()
    for coin_idx in range(i, len(coins)):
        coin = coins[coin_idx]
        for c in range(min(target // coin, coins_table[coin]), 0, -1):

            new_coins_table[coin] -= c
            dfs(new_coins_table, coins, coin_idx + 1, target - (c * coin))
            new_coins_table[coin] += c

    return


T = int(input())
k = int(input())
coins_table = {}
cnt = 0
for _ in range(k):
    coin, n = map(int, input().split())
    coins_table[coin] = n

dfs(coins_table, sorted(coins_table.keys(), reverse=True), 0, T)
print(cnt)