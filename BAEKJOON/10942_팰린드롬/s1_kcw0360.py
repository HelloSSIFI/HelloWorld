import sys
input = sys.stdin.readline


N = int(input())
board = list(map(int, input().split()))
M = int(input())
q = []
for _ in range(M):
    q.append(list(map(int, input().split())))

dp = [[0]*N for _ in range(N)]


for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if board[i] == board[i+1]:
        dp[i][i+1] = 1

for i in range(2, N):
    for j in range(N-i):
        if board[j] == board[i+j] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

answer = []
for s, e in q:
    answer.append('{}\n'.format(dp[s-1][e-1]))

print(''.join(answer))