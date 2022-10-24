import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 플루이드 워셜
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = graph[i][k]+graph[k][j] if graph[i][j] > graph[i][k]+graph[k][j] else graph[i][j]

for _ in range(m):
    s, e, time = map(int, input().split())
    if graph[s-1][e-1] <= time:
        print('Enjoy other party')
    else:
        print('Stay here')