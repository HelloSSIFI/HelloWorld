from collections import defaultdict

T = int(input())
n = int(input())
coins = [list(map(int, input().split())) for _ in range(n)]
coins.sort(reverse=True)

# 행 수: 코인 종류, 열 수: T 크기
dp = [[0]*(T+1) for _ in range(n+1)]
dp[0][0] = 1

# 코인 번호
for i in range(n):

    # 0원부터 T원까지
    for value in range(T+1):
        dp[i+1][value] = dp[i][value]

    # i+1행의 k값을 만드는 방법은 은 i행의 k-코인*사용한 개수에서 올라온다
    for j in range(1, coins[i][1]+1):

        for k in range(j*coins[i][0], T+1):
            dp[i+1][k] += dp[i][k-j*coins[i][0]]

print(dp[n][T])