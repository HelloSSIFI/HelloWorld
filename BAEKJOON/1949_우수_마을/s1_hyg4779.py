def dfs(val, now):
    global ans
    ans = max(val, ans)
    for v in range(1, N+1):
        if v not in graph[now]+[now] and not visit[v]:
            visit[v] = 1
            dfs(val+peo[v], v)
            visit[v] = 0


N = int(input())            # 1번부터 N번마을, 방향이 없는 N-1개의 길
peo = [0]
peo.extend(list(map(int, input().split())))

graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    visit = [0]*(N+1)
    ans = 0
    dfs(0, i)

print(ans)