from collections import deque
import sys
input = sys.stdin.readline


def in_frame(r, c):
    return True if 0 <= r < n and 0 <= c < m else False


k = int(input())
m, n = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]

move = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1), (1, 0), (-1, 0), (0, -1), (0, 1)]

visit = [[[0]*(k+1) for _ in range(m)] for _ in range(n)]
visit[0][0][0] = 1

Q = deque([(0, 0, 0, 0)])

answer = n*m

while Q:
    i, j, mon, hor = Q.popleft()

    if i == n-1 and j == m-1:
        print(mon+hor)
        exit()

    idx = 8 if hor >= k else 0

    for d in range(idx, 12):
        ni, nj = i + move[d][0], j + move[d][1]
        nmon, nhor = mon, hor

        if d < 8:
            nhor += 1
        else:
            nmon += 1

        if in_frame(ni, nj) and field[ni][nj] == 0 and visit[ni][nj][nhor] == 0:
            # print(ni, nj, nmon, nhor)
            visit[ni][nj][nhor] = 1
            Q.append((ni, nj, nmon, nhor))

print(-1)