# Tree dp문제
# 1949 우수마을과 비슷한 문제
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(s):
    visited[s] = True
    for next in tree[s]:
        if not visited[next]:
            dfs(next)
            dp[s][0] += dp[next][1]                     # 현재 노드가 얼리 어답터가 아니라면 -> 자식 노드는 모두 얼리 어답터여야 함
            dp[s][1] += min(dp[next][0], dp[next][1])   # 현재 노드가 얼리 어답터라면 -> 자식 노드는 얼리 어답터 이거나 얼리어답터가 아님(가장 최적해인 것 선택)

n = int(input())
tree = [[] for _ in range(n + 1)]
visited = [False] * (n + 1) 
dp = [[0, 1] for _ in range(n + 1)]                     # [현재 노드가 얼리 어답터가 아닐 때 최적해, 현재 노드가 얼리 어답터일 때 최적해]
for _ in range(n - 1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

dfs(1)
print(min(dp[1][1], dp[1][0]))

