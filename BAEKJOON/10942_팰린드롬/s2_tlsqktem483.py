"""
DP
"""
import sys
input = sys.stdin.readline


ans = []
N = int(input())
board = list(map(int, input().split()))
M = int(input())
dp = [[False]*N for _ in range(N)]

for i in range(N-1, -1, -1):
    for j in range(i, N):
        # 길이 1
        if i == j:
            dp[i][j] = True
        # 길이 2 && 첫문자 끝문자 동일
        elif i + 1 == j and board[i] == board[j]:
            dp[i][j] = True
        # 길이 3 이상 && 첫문자 끝문자 동일
        elif board[i] == board[j]:
            dp[i][j] = dp[i+1][j-1]

for _ in range(M):
    S, E = map(int, input().split())
    print(1 if dp[S-1][E-1] else 0)


