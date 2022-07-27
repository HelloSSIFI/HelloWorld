import sys
sys.setrecursionlimit(10**9)


n, m = map(int, input().split())

people = []
for i in range(n):
    people.append(int(input()))

dp = [[-1 for i in range(m)] for j in range(n)]


def dfs(idx, now):
    if dp[idx][now] != -1:
        return dp[idx][now]
    elif idx == n-1:
        return 0
    else:
        if now + 1 + people[idx + 1] < m:
            dp[idx][now] = min(dfs(idx+1, now+1+people[idx+1]), dfs(idx+1, people[idx+1]-1) + (m-(now+1))**2)
        else:
            dp[idx][now] = dfs(idx+1, people[idx+1]-1)+(m-(now+1))**2

    return dp[idx][now]


print(dfs(0, people[0]-1))