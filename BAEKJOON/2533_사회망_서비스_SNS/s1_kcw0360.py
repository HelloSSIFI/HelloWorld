import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x):
    visited[x] = 1    # 현 위치 방문 체크

    for i in graph[x]:
        if not visited[i]:    # 방문하지 않은 곳은 재귀 수행
            dfs(i)    # 재귀 수행을 통해 Leaf node까지 도달
            dp[x][0] += dp[i][1]    # 현재 node가 early adaptor가 아니라면 child는 무조건 early adaptor
            dp[x][1] += min(dp[i][0], dp[i][1])    # 현재 node가 early adaptor라면 child의 early adaptor 관계없이 적은 케이스 가져온다.

N = int(input())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
dp = [[0, 1] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

print(min(dp[1][0], dp[1][1]))