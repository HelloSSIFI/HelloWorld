N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]

for diagonal in range(1, N):
    for i in range(0, N-diagonal):
        j = i + diagonal
        if diagonal == 1:
            dp[i][j] = arr[i][0] * arr[j][0] * arr[j][1]
            continue

        dp[i][j] = float('inf')

        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + arr[i][0] * arr[k][1] * arr[j][1])

print(dp[0][N-1])

# 참고 url: https://dapsu-startup.tistory.com/entry/%EB%B0%B1%EC%A4%80BAEKJOON-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-11049-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython