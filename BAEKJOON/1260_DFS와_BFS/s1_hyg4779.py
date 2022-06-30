from collections import deque
import sys
input=sys.stdin.readline


N, M, V = map(int, input().split())             # 정점 수, 간선 수, 시작 정점
graph = [list() for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())            # 연결된 정점
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()


def dfs(s):
    visit[s] = True
    print(s, end=" ")
    for idx in graph[s]:
        if not visit[idx]:
            dfs(idx)


def bfs(s):
    q = deque([s])
    visit[s] = True
    while q:
        now = q.popleft()
        print(now, end=" ")
        for idx in graph[now]:
            if not visit[idx]:
                q.append(idx)
                visit[idx] = True


visit = [False]*(N+1)
dfs(V)
print()
visit = [False]*(N+1)
bfs(V)
