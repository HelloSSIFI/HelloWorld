N = int(input())
dp = list(range(7))

for _ in range(N - 6):                                      # 3번째 전 값을 복사한 것과, 4번째 전 값을 복사2번, 
    dp.append(max(dp[-5] * 4, dp[-4] * 3, dp[-3] * 2))      # 5번째 전 값을 복사 3번 한 값을 비교하여 큰 값을 선택

print(dp[N])
