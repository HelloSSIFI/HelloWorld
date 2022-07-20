import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1

    for i in villages[x]:
        if not visited[i]:
            dfs(i)
            dp[x][0] += max(dp[i][0], dp[i][1])
            dp[x][1] += dp[i][0]

N = int(input())
population = [0] + list(map(int, input().split()))
villages = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dp = [[0, population[i]] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    villages[a].append(b)
    villages[b].append(a)

dfs(1)

print(max(dp[1][0], dp[1][1]))