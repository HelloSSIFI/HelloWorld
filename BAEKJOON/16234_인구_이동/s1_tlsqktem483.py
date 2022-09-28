import sys
input = sys.stdin.readline


def dfs():
    union = [[0]*N for _ in range(N)]
    checked = 0
    idx = 1
    flag = False
    for r in range(N):
        for c in range(N):
            if union[r][c]:
                continue

            org = [[r, c]]
            stack = [[r, c]]
            union[r][c] = idx
            sum_value = graph[r][c]
            checked += 1
            while stack:
                i, j = stack.pop()

                for di in d:
                    ni, nj = i + di[0], j + di[1]
                    if 0 <= ni < N and 0 <= nj < N and not union[ni][nj] and L <= abs(graph[i][j]-graph[ni][nj]) <= R:
                        stack.append([ni, nj])
                        union[ni][nj] = idx
                        org.append([ni, nj])
                        sum_value += graph[ni][nj]
                        checked += 1

            for i, j in org:
                if len(org) > 1:
                    flag = True
                graph[i][j] = sum_value // len(org)

            idx += 1

            if checked == N*N:
                return flag
    return flag

ans = 0
N, L, R = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

stoped = True
while stoped:
    stoped = dfs()
    if stoped:
        ans += 1
print(ans)