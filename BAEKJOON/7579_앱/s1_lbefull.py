N, M = map(int, input().split())
mem = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
K = N * max(cost) + 1
dp = [[0] * K for _ in range(N + 1)]
result = K

for i in range(1, N + 1):                               # dp의 첫째 행부터 순회
	for j in range(min(result, cost[i])):               # 각 행의 열을 현재 cost전까지 순회
		dp[i][j] = dp[i - 1][j]                         # 이전 값들을 그대로 가져옴
	for j in range(cost[i], result):                    # cost부터 이전 최소값까지 반복하면서 M을 넘는 최소 cost를 저장
		dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + mem[i])
		if dp[i][j] >= M:
			result = j
			break

print(result)
