import sys
input = sys.stdin.readline


T = int(input())
k = int(input())
coin = []
for _ in range(k):
    p, n = map(int, input().split())
    coin.append([p, n])

dp = [0] * (T + 1)
dp[0] = 1
for p, n in coin:                           # 모든 동전과 개수를 탐색
    for i in range(T, -1, -1):              # 중복을 피하기 위해 큰 금액부터 탐색
        if not dp[i]:                       # 현재 i원을 만드는 경우의 수가 없다면 다음반복
            continue

        for j in range(1, n + 1):           # 동전의 개수만큼 반복
            if i + p * j > T:               # i원에 현재 동전 p를 j만큼 더했을 때 목표금액 T를 넘어가면
                break                       # 반복종료
            dp[i + p * j] += dp[i]          # 아니라면 해당 위치에 현재 경우의 수를 더해줌

print(dp[T])
