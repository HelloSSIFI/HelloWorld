"""
DFS
메모리 초과
"""
import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

N, M, K = map(int, input().split())
di = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # 상 우 하 좌

way_map = [["."]*M for _ in range(N)]
visited = [[False]*M for _ in range(N)]
ans = []

for _ in range(K):
    r, c = map(int, input().split())
    way_map[r-1][c-1] = "#"



def dfs(i, j, cnt, v):
    global ans
    flag = False

    for d in di:
        temp = [item[:] for item in v]
        next_i, next_j = i + d[0], j + d[1]

        if 0 <= next_i < N and 0 <= next_j < M and way_map[next_i][next_j] == "#" and not v[next_i][next_j]:
            temp[next_i][next_j] = True
            flag = True
            dfs(next_i, next_j, cnt+1, temp)

    if not flag:
        ans.append(cnt)
        return


for i in range(N):
    for j in range(M):
        if way_map[i][j] == "#":
            temp = [item[:] for item in visited]
            temp[i][j] = True
            dfs(i, j, 1, temp)

print(max(ans))
