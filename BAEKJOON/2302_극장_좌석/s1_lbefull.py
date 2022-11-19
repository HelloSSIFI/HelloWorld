N = int(input())
M = int(input())
dp = [0] * (N + 1)
fixed = [0] * (N + 1)
for _ in range(M):
    fixed[int(input())] = 1                                         # 고정 좌석을 fixed에 표시

dp[0] = dp[1] = 1
for i in range(2, N + 1):                                           # 현재 좌석의 경우의 수는
    dp[i] = dp[i - 1]                                               # 현재 좌석과 이전 좌석이 자리교체가 가능한 경우
    if not fixed[i] and not fixed[i - 1]: dp[i] += dp[i - 2]        # 교체 할 때의 경우와 교체 하지 않을 때의 경우가 있으므로 전전좌석의 경우의 수가 더해지게 됨

print(dp[-1])
