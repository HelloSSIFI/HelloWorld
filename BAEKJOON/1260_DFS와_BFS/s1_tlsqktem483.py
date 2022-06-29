import sys
from collections import defaultdict, deque


def dfs(s):
    ans = []

    while len(ans) < N:
        if not s:
            break
        node = s.pop()
        if node not in ans:
            ans.append(node)

        for next in sorted(graph[node], reverse=True):
            if next not in ans:
                s.append(next)
    return ans


def bfs(q):
    ans = []

    while len(ans) < N:
        if not q:
            break
        node = q.popleft()
        if node not in ans:
            ans.append(node)

        for next in sorted(graph[node]):
            if next not in ans:
                q.append(next)
    return ans


N, M, V = map(int, sys.stdin.readline().split())
graph = defaultdict(list)

for _ in range(M):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

print(*dfs([V]))
print(*bfs(deque([V])))