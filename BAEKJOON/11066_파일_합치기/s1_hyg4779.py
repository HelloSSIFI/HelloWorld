import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [0]+list(map(int, input().split()))

    # 누적합 구해주기
    for i in range(1, n+1):
        arr[i] += arr[i-1]

    # dp[i][j]: i에서 j까지 합하는 데 최소 비용
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for idx in range(2, n+1):
        for j in range(1, n+2-idx):
            dp[j][j+idx-1] = min([dp[j][j+k]+dp[j+k+1][j+idx-1] for k in range(idx-1)])+(arr[j+idx-1]-arr[j-1])

    print(dp[1][n])