import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())            # 1번부터 N번마을, 방향이 없는 N-1개의 길
peo = [0]+list(map(int, input().split()))
graph = [[] for _ in range(N+1)]


for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[0, p] for p in peo]
visit = [0]*(N+1)


def dfs(n):
    visit[n] = 1
    for i in graph[n]:
        if not visit[i]:
            dfs(i)
            dp[n][0] += max(dp[i][0], dp[i][1])
            dp[n][1] += dp[i][0]

dfs(1)
print(max(dp[1][0], dp[1][1]))