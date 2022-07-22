import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(s):
    global visited, dp
    visited[s] = True

    for node in tree[s]:
        if not visited[node]:
            dfs(node)
            dp[s][0] += max(dp[node][0], dp[node][1])
            dp[s][1] += dp[node][0]


N = int(input())
towns = [0] + list(map(int, input().split()))
visited = [False for _ in range(N+1)]
dp = [[0, towns[i]] for i in range(N+1)]
tree = defaultdict(list)

for _ in range(N-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

dfs(1)
print(max(dp[1][0], dp[1][1]))