import sys
input = sys.stdin.readline

c, n = map(int, input().split())
info = sorted([tuple(map(int, input().split())) for _ in range(n)])

# 고객의 수는 비용당 최대 100명
dp = [0] + [1000000] * (c + 100)

# 출력 값
res = 1000000

# 비용당 고객
for cost, client in info:
    # 현재 모을 수 있는 고객부터 최대 dp 길이만큼
    for i in range(client, len(dp)):
        # i명 모으는데 필요한 비용, i명 - client 의 비용에 cost를 더한 비용 중
        # 최솟값을 갱신
        dp[i] = min(dp[i - client] + cost, dp[i])
        # 현재 i명이 c명 이상이면 출력값 갱신
        if i >= c:
            res = min(dp[i], res)
print(res)
