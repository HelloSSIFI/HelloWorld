"""
아이디어 : DFS + visited 에 key 갯수로 판별
시간초과
"""
import sys
input = sys.stdin.readline


def dfs(i, j, v, k, cnt):
    global ans
    if cnt >= ans:
        return

    if graph[i][j] == '1':
        if ans > cnt:
            ans = cnt
        return

    for di in d:
        ni, nj = i + di[0], j + di[1]

        if (ni, nj, len(k)) not in v and 0 <= ni < N and 0 <= nj < M:
            if graph[ni][nj] in ['.', '0', '1']:
                dfs(ni, nj, v+[(ni, nj, len(k))], k, cnt+1)
            elif graph[ni][nj] in ['a', 'b', 'c', 'd', 'e', 'f']:
                ck = k.copy()
                ck.add(graph[ni][nj].upper())
                dfs(ni, nj, v + [(ni, nj, len(ck))], ck, cnt + 1)
            elif graph[ni][nj] in ['A', 'B', 'C', 'D', 'E', 'F'] and graph[ni][nj] in k:
                dfs(ni, nj, v + [(ni, nj, len(k))], k, cnt + 1)


N, M = map(int, input().split())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
graph = [list(input()) for _ in range(N)]
start = (0, 0)
end = (0, 0)
ans = float('inf')

for i in range(N):
    for j in range(M):
        if graph[i][j] == '0':
            start = (i, j)
        elif graph[i][j] == '1':
            end = (i, j)

dfs(start[0], start[1], [(start[0], start[1], 0)], set(), 0)
print(ans if ans != float('inf') else -1)