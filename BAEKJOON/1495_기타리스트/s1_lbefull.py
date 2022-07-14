N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [{S}] + [set() for _ in range(N)]
result = -1

for i in range(1, N + 1):               # 곡을 차례로 순회
    for el in dp[i - 1]:                # 이전 곡에 가능한 볼륨을 순회
        if 0 <= el + V[i - 1] <= M:     # 현재 차이를 더하는 것이 범위 내에 있으면 저장
            dp[i].add(el + V[i - 1])
        if 0 <= el - V[i - 1] <= M:     # 현재 차이를 빼는 것이 범위 내에 있으면 저장
            dp[i].add(el - V[i - 1])

if dp[N]:                               # 반복이 끝나고 저장된 것이 있으면
    result = max(dp[N])                 # 최고값을 가져옴

print(result)
