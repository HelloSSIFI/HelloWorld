import sys
from collections import deque
input = sys.stdin.readline


N, M, V = map(int, input().split())         #N: 정점 개수, M: 간선 개수, V: 출발 지점

graph = [[] for _ in range(N + 1)] 

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

# DFS
stack = [V]
dfs_visited = [False] * (N + 1)
dfs_visited[V] = True
print(V, end = ' ')
while stack:
    now = stack.pop()
    if not dfs_visited[now]:
        dfs_visited[now] = True
        print(now, end = ' ')
    
    graph[now].sort(reverse=True)
    for next in graph[now]:
        if not dfs_visited[next]:
            stack.append(next)

print()
# BFS
queue = deque()
bfs_visited = [False] * (N + 1)
queue.append(V)
bfs_visited[V] = True
print(V, end = ' ')
while queue:
    here = queue.popleft()

    if not bfs_visited[here]:
        bfs_visited[here] = True
        print(here, end = ' ')

    graph[here].sort()
    for next in graph[here]:
        if not bfs_visited[next]:
            queue.append(next)

