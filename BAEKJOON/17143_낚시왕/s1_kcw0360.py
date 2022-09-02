import sys
input = sys.stdin.readline


R, C, M = map(int, input().split())
sea = [[0]*C for _ in range(R)]
sharks = []
result = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())    # 행, 열, 속력, 방향, 크기
    sea[r-1][c-1] = [s, d, z]

# direction = [[-1, 0], [1, 0], [0, 1], [0, -1]]    # 상 하 우 좌
direction = {1: -1, 2: 1, 3: 1, 4: -1}
for king in range(C):    # 한칸씩 이동 하며 낚시
    # 해당 열에 있는 첫번째 상어 낚시 하기
    for i in range(R):
        if sea[i][king]:    # 상어가 존재한다면 낚시 후 (크기 더하기) 0 처리
            result += sea[i][king][2]
            sea[i][king] = 0
            break
    if king == C-1:
        break

    # 상어 이동
    temp_sea = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if sea[i][j]:
                y, x = i, j
                vel = sea[i][j][0]
                d = sea[i][j][1]
                if d == 1 or d == 2:
                    flag = True
                    while flag:
                        y += direction[d] * vel
                        if y < 0:
                            vel = 0 - y
                            y = 0
                            d = 2
                        elif y > R-1:
                            vel = y - R + 1
                            y = R-1
                            d = 1
                        else:
                            flag = False
                elif d == 3 or d == 4:
                    flag = True
                    while flag:
                        x += direction[d] * vel
                        if x < 0:
                            vel = 0 - x
                            x = 0
                            d = 3
                        elif x > C-1:
                            vel = x - C + 1
                            x = C-1
                            d = 4
                        else:
                            flag = False
                sea[i][j][1] = d
                # 동일 좌표에 상어가 있다면 잡아 먹고 큰 상어 저장
                if temp_sea[y][x]:
                    if temp_sea[y][x][2] < sea[i][j][2]:
                        temp_sea[y][x] = sea[i][j]
                else:
                    temp_sea[y][x] = sea[i][j]
    sea = temp_sea

print(result)
