import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
memory_table = [0] + list(map(int, input().split()))
cost_table = [0] + list(map(int, input().split()))

max_cost = sum(cost_table)

dp = [[0] * (max_cost + 1) for _ in range(N + 1)]   # dp[i][j] : i번째 까지 앱을 고를 때, j의 비용으로 얻을 수 있는 최대 메모리


for i in range(1, N + 1):
    max_j = sum(cost_table[:i + 1])
    for j in range(max_cost + 1):
        if j >= cost_table[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - cost_table[i]] + memory_table[i])    # i - 1번째 앱까지 탐색했을 때 현재 앱의 비용을 뺀 만큼의 최대 메모리에서 현재 앱의 메모리를 더한 값이 더 크다면 갱신(j 비용의 최대 메모리)
        dp[i][j] = max(dp[i][j], dp[i - 1][j])                                          # 같은 비용으로 i번째보다 i-1번째 앱까지 탐색했을 때 메모리가 더 크다면 -> 현재 i번째 앱의 j번째 비용의 최대 메모리 갱신
    
for k in range(max_cost + 1):
    if dp[N][k] >= M:
        print(k)
        break  