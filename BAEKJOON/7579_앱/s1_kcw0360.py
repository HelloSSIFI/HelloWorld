N, M = map(int, input().split())    # N: 앱 수, M: 필요한 메모리
memory = list(map(int, input().split()))    # 각 앱의 메모리 크기
cost = list(map(int, input().split()))    # 비활성화 했을 경우 비용
sum_cost = sum(cost)    # 모든 메모리를 비활성화 했을 때 (최대 비용)
dp = [[0]*sum_cost for _ in range(N+1)]
answer = sum_cost

for i in range(1, N+1):
    for j in range(sum_cost):
        if j < cost[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-cost[i-1]] + memory[i-1])

        if dp[i][j] >= M and answer > j:    # 최소값 확인
            answer = j

print(answer)