import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(s):
    global visited, dp
    visited[s] = True
    dp[s][0] = 1

    for node in graph[s]:
        if not visited[node]:
            dfs(node)
            dp[s][0] += min(dp[node][0], dp[node][1])
            dp[s][1] += dp[node][0]


N = int(input().rstrip())
graph = [[] for _ in range(N+1)]
dp = [[0, 0] for _ in range(N+1)]
visited = [False for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(1)
print(min(dp[1][0], dp[1][1]))