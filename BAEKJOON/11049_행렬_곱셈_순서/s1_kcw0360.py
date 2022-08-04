N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N-i):
        tmp = i + j

        if j == tmp:
            continue

        dp[j][tmp] = 9876543210
        for k in range(j, tmp):
            dp[j][tmp] = min(dp[j][tmp], dp[j][k] + dp[k+1][tmp] + matrix[j][0] * matrix[k][1] * matrix[tmp][1])

print(dp[0][-1])