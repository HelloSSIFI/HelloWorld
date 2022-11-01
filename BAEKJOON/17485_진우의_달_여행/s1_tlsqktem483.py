"""
완전탐샘 -> 시간초과 O(3*N*M) ~= 3,000,000
3방향 추가한 DP and 이전 방향 제외 알고리즘
"""
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')]*3 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        if i == 0:
            for idx in range(3):
                dp[i][j][idx] = graph[i][j]

        else:
            if j == 0:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i][j]
                dp[i][j][1] = dp[i - 1][j][0] + graph[i][j]

            elif j == M-1:
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + graph[i][j]
                dp[i][j][1] = dp[i - 1][j][2] + graph[i][j]

            else:
                dp[i][j][0] = min(dp[i - 1][j + 1][1], dp[i - 1][j + 1][2]) + graph[i][j]
                dp[i][j][1] = min(dp[i - 1][j][0], dp[i - 1][j][2]) + graph[i][j]
                dp[i][j][2] = min(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + graph[i][j]

ans = float('inf')

for c in range(M):
    ans = min(ans, min(dp[N-1][c][:]))
print(ans)