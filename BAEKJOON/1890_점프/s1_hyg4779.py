import sys
N = int(input())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

# dp그래프로 현위치에서 점프한 위치로 갈 수 있는 이동 경우 수를 추가하며 이동
for i in range(N):
    for j in range(N):

# 끝 점에 도착하면 바로 break
# 끝 점에 break를 안 하면 한 번 더 점프해서 값을 추가함

        if i == N-1 and j == N-1:
            print(dp[N-1][N-1])
            break

        zump = arr[i][j]

        if i+zump < N:
            dp[i+zump][j] += dp[i][j]
        if j+zump < N:
            dp[i][j+zump] += dp[i][j]