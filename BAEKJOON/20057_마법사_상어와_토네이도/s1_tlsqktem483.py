import sys
from math import trunc
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
d = [(0, -1), (1, 0), (0, 1), (-1, 0)]
percent = [1, 1, 2, 2, 7, 7, 10, 10, 5]
i, j = N // 2, N // 2
turn = 0
d_idx = 0
m = 1
ans = 0
ni, nj = i, j
while [ni, nj] != [0, 0]:
    di = d[d_idx]
    for _ in range(m):
        if d_idx in [0, 2]:
            t = [[ni-1, nj], [ni+1, nj], [ni-2, nj+di[1]], [ni+2, nj+di[1]], [ni-1, nj+di[1]], [ni+1, nj+di[1]], [ni-1, nj+2*di[1]], [ni+1, nj+2*di[1]], [ni, nj+3*di[1]], [ni, nj+2*di[1]]]
        else:
            t = [[ni, nj-1], [ni, nj+1], [ni+di[0], nj-2], [ni+di[0], nj+2], [ni+di[0], nj-1], [ni+di[0], nj+1], [ni+2*di[0], nj-1], [ni+2*di[0], nj+1], [ni+3*di[0], nj], [ni+2*di[0], nj]]
        if ni+di[0] >= N or nj+di[1] >= N or ni+di[0] < 0 or nj+di[1] < 0:
            break
        ni += di[0]
        nj += di[1]
        total = graph[ni][nj]
        sum_v = 0
        if not total:
            continue
        for t_idx in range(9):
            ti, tj = t[t_idx]
            amount = trunc(total*(percent[t_idx]/100))
            if 0 <= ti < N and 0 <= tj < N:
                graph[ti][tj] += amount
            else:
                ans += amount
            sum_v += amount
        ti, tj = t[-1]
        amount = total - sum_v
        if 0 <= ti < N and 0 <= tj < N:
            graph[ti][tj] += amount
        else:
            ans += amount

    turn += 1
    if turn % 2 == 0:
        m += 1
    d_idx = (d_idx+1) % 4
print(ans)

