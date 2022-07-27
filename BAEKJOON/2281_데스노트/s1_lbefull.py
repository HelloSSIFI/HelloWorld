import sys
input = sys.stdin.readline


N, M = map(int, input().split())
dp = [dict() for _ in range(N)]                 # 각 이름마다 해당하는 칸에 가장 적은 빈공간을 저장할 dp
dp[0][int(input())] = 0                         # 처음 이름을 칸에 맞는 위치에 0으로 저장
for i in range(1, N):                           # 이름을 순회하면서 현재 이름을 새로운 줄에 적을 때
    l = int(input())                            # 이전 이름들 중 최소값을 가져옴
    dp[i][l] = min(map(lambda x: x[1] + (M - x[0]) ** 2, dp[i - 1].items()))
    for k, v in dp[i - 1].items():              # 그리고 이전 이름들 중 현재 이름을 쓸 칸이 남는다면
        if k + l < M:                           # 현재 이름을 추가
            dp[i][k + l + 1] = dp[i - 1][k]

print(min(dp[-1].values()))
