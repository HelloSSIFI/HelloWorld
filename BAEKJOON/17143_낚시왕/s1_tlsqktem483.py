"""
Python3 에서는 실패, Pypy3 에서 통과
"""
import sys
input = sys.stdin.readline


def move():
    global a

    g = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if a[i][j]:
                r, c = i, j
                s, d, z = a[i][j][0]
                dist = s

                while 0 < dist:
                    nr = r + di[d][0]
                    nc = c + di[d][1]

                    if 0 <= nr < R and 0 <= nc < C:
                        r, c = nr, nc
                        dist -= 1
                    # 벽과 충돌
                    else:
                        if d in [0, 2]:
                            d += 1
                        elif d in [1, 3]:
                            d -= 1
                        continue

                g[r][c].append([s, d, z])
    a = g[:][:]


R, C, M = map(int, input().split())
di = [(-1, 0), (1, 0), (0, 1), (0, -1)]     # 상 우 하 좌
# 시뮬레이션 맵
a = [[[] for _ in range(C)] for _ in range(R)]
ans = 0
for idx in range(M):
    r, c, s, d, z = map(int, input().split())
    a[r-1][c-1].append([s, d-1, z])

# 1. 낙시왕 이동
for j in range(C):
    # 2. 가장 가까운 상어 포획
    for i in range(R):
        if a[i][j]:
            ans += a[i][j][0][2]
            a[i][j].remove(a[i][j][0])
            break

    # 3. 상어 이동
    move()

    for x in range(R):
        for y in range(C):
            if len(a[x][y]) > 1:
                a[x][y].sort(key=lambda x:x[2], reverse=True)
                while len(a[x][y]) > 1:
                    a[x][y].pop()


print(ans)
