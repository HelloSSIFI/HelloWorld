# pypy3 통과

import sys
from collections import deque
input = sys.stdin.readline


# 먼지 확산
def spread(house):
    dusts = deque()

    # 먼지 위치 탐색
    for i in range(R):
        for j in range(C):
            if house[i][j] > 0:
                dusts.append((i, j, house[i][j]))                # (행 위치, 열 위치, 먼지 양)

    spread_dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]             # 상 하 좌 우
    while dusts:
        r, c, dust = dusts.popleft()
        cnt = 0
        for d in spread_dirs:
            nr = r + d[0]
            nc = c + d[1]
            if 0 <= nr < R and 0 <= nc < C and house[nr][nc] != -1:
                house[nr][nc] += dust // 5 
                cnt += 1
        house[r][c] -= (dust // 5) * cnt
        
                


# 공기청정기의 바람이 지나는 경로 대로 먼지 포집 후 교체
def clean(house, cleaner, direction, dirs):
    i, j = cleaner[direction]
    wind = deque([(i, j)])

    control = dirs[direction]
    d = 0
    dusts_box = deque()                   # 먼지 보관함
    while wind:
        sr, sc = wind.popleft()
        r, c = sr, sc

        r += control[d][0]
        c += control[d][1]

        while direction == 'up' and 0 <= r <= i and 0 <= c < C:
            if house[r][c] > 0:
                if dusts_box:
                    # 이미 먼지보관함에 먼지가 있는 상태라면
                    # 현재 위치의 먼지를 포집하고, 먼저 들어와있던 먼지를 내보냄
                    dusts_box.append(house[r][c])
                    house[r][c] = dusts_box.popleft()

                else:
                    # 먼지 보관함에 먼지가 없으면 그냥 포집
                    dusts_box.append(house[r][c])
                    house[r][c] = 0
            elif house[r][c] == 0 and dusts_box:
                # 현재 위치에 아무 먼지가 없지만 보관함에 먼지가 있는 상태라면
                # 보관함의 먼지를 내보냄
                house[r][c] = dusts_box.popleft()

            sr, sc = r, c
            r += control[d][0]
            c += control[d][1]
            
        while direction == 'down' and i <= r < R and 0 <= c < C:
            if house[r][c] > 0:
                if dusts_box:
                    # 이미 먼지보관함에 먼지가 있는 상태라면
                    # 현재 위치의 먼지를 포집하고, 먼저 들어와있던 먼지를 내보냄
                    dusts_box.append(house[r][c])
                    house[r][c] = dusts_box.popleft()
                else:
                    # 먼지 보관함에 먼지가 없으면 그냥 포집
                    dusts_box.append(house[r][c])
                    house[r][c] = 0
            elif house[r][c] == 0 and dusts_box:
                # 현재 위치에 아무 먼지가 없지만 보관함에 먼지가 있는 상태라면
                # 보관함의 먼지를 내보냄
                house[r][c] = dusts_box.popleft()

            sr, sc = r, c
            r += control[d][0]
            c += control[d][1]

        d = (d + 1) % 4
        if (sr, sc) != (i, j):
            wind.append((sr, sc))



R, C, T = map(int, input().split())
house = [list(map(int, input().split())) for _ in range(R)]

cleaner = {
    'up' : [],
    'down' : []
}


for i in range(R):
    if cleaner['up'] and cleaner['down']:
        break
    for j in range(C):
        if house[i][j] == -1 and not cleaner['up']:
            cleaner['up'] = (i, j)
        elif house[i][j] == -1 and not cleaner['down']:
            cleaner['down'] = (i, j)
        

dirs = {
    'up' : [[0, 1], [-1, 0], [0, -1], [1, 0]],               # 반 시계방향 회전
    'down' : [[0, 1], [1, 0], [0, -1], [-1, 0]]              # 시계방향 회전
}


t = 1
while t <= T:
    spread(house)
    clean(house, cleaner, 'up', dirs)
    clean(house, cleaner, 'down', dirs) 
    t += 1

total = 0
for i in range(R):
    for j in range(C):
        if house[i][j] > 0:
            total += house[i][j]
print(total)
