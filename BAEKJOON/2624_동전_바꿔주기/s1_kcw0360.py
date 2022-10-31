import sys
input = sys.stdin.readline


T = int(input())
k = int(input())
dp = [0] * (T+1)    # 0원부터 T원 까지의 dp 생성
dp[0] = 1    # 0원은 아무 동전도 사용하지 않은 경우
for _ in range(k):
    coin, cnt = map(int, input().split())
    for price in range(T, 0, -1):    # 역순으로 탐색(순서대로 진행하는 경우 누적으로 인한 오류 발생)
        for num in range(1, cnt+1):    # 동전 개수 만큼 반복
            if price - coin * num >= 0:    # idx(만들수 있는 금액) 벗어나지 않는 범위
                # 현재 금액의 경우의 수 += 현재 입력받은 동전을 num개 사용해서 금액을 제외한 금액을 만들 수 있는 경우의 수
                dp[price] += dp[price - coin * num]

print(dp[T])