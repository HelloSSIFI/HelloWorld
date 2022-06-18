"""
위상정렬
O(N + M)
"""

from collections import deque
n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
ans = []
queue = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for st in range(1, n+1):
    if indegree[st] == 0:
        queue.append(st)

while queue:
    c = queue.popleft()
    ans.append(c)

    for j in graph[c]:
        indegree[j] -= 1
        if indegree[j] == 0:
            queue.append(j)

print(*ans)