import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(start):
    visited[start] = 1
    
    for next in tree[start]:
        if not visited[next]:
            dfs(next)
            dp[start][0] += max(dp[next][1], dp[next][0])
            dp[start][1] += dp[next][0]

n = int(input())
towns = [0] + list(map(int, input().split()))
tree = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)
visited = [0] * (n + 1)
dp = [[0, towns[i]] for i in range(n + 1)]
dfs(1)
print(max(dp[1][0], dp[1][1]))