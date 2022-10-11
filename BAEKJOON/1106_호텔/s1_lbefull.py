C, N = map(int, input().split())
dp = [0] + [100001] * C
for _ in range(N):
    cost, guest = map(int, input().split())         # 사람이 홍보해서 늘어나는 최소 고객보다 작으면 dp에 저장된 값과 cost 중 작은 값 선택
    for i in range(1, C + 1):                       # 최소 고객보다 많으면, 현재 i명에서 최소고객을 뺀 비용에 cost를 더한 값과 dp에 저장된 값 중 작은 값을 선택
        dp[i] = min(dp[i], cost) if i < guest else min(dp[i], dp[i - guest] + cost)
print(dp[C])
