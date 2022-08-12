import sys
input = sys.stdin.readline


N = int(input())                                                    # dp[r][c]는 r행 ~ c열까지 행렬 계산 중 최소값을 저장
mat = [list(map(int, input().split())) for _ in range(N)]           # 새로운 행렬이 생기면 그 최소값은 각각 (1 / n) (2 / n - 1) ... (n / 1) 으로 그룹을 나누었을 때
dp = [[0] * N for _ in range(N)]                                    # 각각의 최소값에 나뉜지점에서 행렬 계산한 값을 더해주면 되고 모든 값 중 최소값을 선택

for i in range(1, N):
    for j in range(i - 1, -1, -1):
        min_v = 2 ** 31 - 1
        for k in range(i - j):
            temp = dp[i - k][i] + dp[j][i - 1 - k]
            temp += mat[j][0] * mat[i - 1 - k][1] * mat[i][1]
            min_v = min(min_v, temp)
        dp[j][i] = min_v

print(dp[0][-1])
