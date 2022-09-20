"""
모든 Cluster 다 돌면 RuntimeError
"""
import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def arrange():
    global cave

    # Clustering
    c = [[0] * C for _ in range(R)]
    number_c = 0
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x' and not c[i][j]:
                number_c += 1
                c[i][j] = number_c
                q = deque()
                q.append([i, j, number_c])

                while q:
                    row, col, n = q.popleft()

                    for di in d:
                        nr, nc = row + di[0], col + di[1]
                        if 0 <= nr < R and 0 <= nc < C and cave[nr][nc] == 'x' and not c[nr][nc]:
                            c[nr][nc] = n
                            q.append([nr, nc, n])

    dist = defaultdict(lambda: R)
    for i in range(R):
        for j in range(C):
            if cave[i][j] == 'x':
                n = c[i][j]

                if i == R-1:
                    dist[n] = 0
                elif c[i+1][j] != n:
                    for r in range(i+1, R):
                        if c[r][j] == n:
                            break
                        elif c[r][j]:
                            dist[n] = min(dist[n], r-(i+1))
                            break
                    if dist[n] == R:
                        dist[n] = R - (i+2)

    # Gravity
    for n, v in dist.items():
        if v:
            for i in range(R-1, -1, -1):
                for j in range(C):
                    if c[i][j] == n and dist[n]:
                        cave[i][j] = '.'
                        cave[i+dist[n]][j] = 'x'
            break


def crash(arrow, i):
    """
    :param arrow: 화살 차례 (0=>창영, 1=>상근)
    :param i: 화살 던질 row 값
    """
    global cave
    a = 1 if arrow == 0 else -1
    j = 0 if arrow == 0 else C-1

    while 0 <= j < C:
        if cave[i][j] == 'x':
            cave[i][j] = '.'
            arrange()
            break
        j += a


R, C = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(R)]
N = int(input().rstrip())
shoot = list(map(int, input().split()))
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]

for s in range(len(shoot)):
    # crash 0->창영, 1->상근
    if s % 2 == 0:
        crash(0, -shoot[s])
    else:
        crash(1, -shoot[s])

for i in range(R):
    print(''.join(cave[i][:]))