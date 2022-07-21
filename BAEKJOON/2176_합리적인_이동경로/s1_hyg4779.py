import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visit = set()
adopt = set()


def dfs(n):

    visit.add(n)
    if len(graph[n])<=1:
        return True

    for i in graph[n]:
        if i not in visit:
            if dfs(i):
                adopt.add(n)
            elif not i in adopt:
                adopt.add(n)
    return False


for i, start in enumerate(graph):
    if len(start)>1:
        dfs(i)
        break

if N==2:
    print(1)
else:
    print(len(adopt))

