import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)

for i in range(1, N + 1):
    day, money = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])                               # 이전날과 현재 중 큰 값을 가져옴
    if i + day > N + 1:                                         # 현재 상담이 퇴사 후에도 이어진다면
        continue                                                # continue

    dp[i + day - 1] = max(dp[i + day - 1], dp[i - 1] + money)   # 상담 완료 날에 저장된 값과 상담을 했을 때 값중 큰 값을 남겨둠

print(dp[N])
