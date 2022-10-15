'''
상어 0,0 물고기 먹고 시작
번호가 작은 물고기 부터 이동
한칸씩 이동 (빈칸 or 다른 물고기가 있는칸: 위치 스왑) 상어있는칸 안됨
이동할 수 있는 칸을 찾을때까지 45도 반시계 회전, 이동 못하면 제자리

물고기 이동 후 상어 이동
한번에 여러칸 이동가능
물고기 있는 칸으로 이동했다면 먹고, 방향을 가짐
이동하는 중에 있는 칸의 물고기는 먹지 않음
'''
# 반시계 방향 회전 8방향
dx = (-1, -1, 0, 1, 1, 1, 0, -1)
dy = (0, -1, -1, -1, 0, 1, 1, 1)

# 물고기 번호 정보 배열
fishes = [[] for _ in range(17)]
# 바다 배열
sea = [[0]*4 for _ in range(4)]

for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        # 바다에 있는 물고기 번호
        sea[i][j] = line[2*j]
        # 물고기 정보: 위치, 방향
        fishes[line[2*j]] = [i, j, line[2*j+1]-1]


# 바다, 상어 위치 및 방향, 물고기 정보, 먹은 물고기 번호 최대값
def move(field, r, c, p, info, res):
    # 1. 상어 물고기 먹음
    # 현재 상어 위치 물고기 먹음
    num = field[r][c]
    res += num
    p = info[num][2]

    # 물고기 정보와 바다에서 물고기 삭제
    info[num], field[r][c] = False, False

    # 2. 물고기 이동
    for f in range(1, 17):
        # 죽은 물고기 continue
        if info[f] == False:continue

        # 위치와 방향
        x, y, d = info[f]
        idx = 0
        while idx < 8:
            nx, ny = x + dx[(d+idx)%8], y + dy[(d+idx)%8]
            # 격자 안이고 상어랑 겹치지 않는다면 == 이동할 수 있다
            if 0 <= nx < 4 and 0 <= ny < 4 and (nx, ny) != (r, c):

                # 빈칸인 경우
                if not field[nx][ny]:
                    # 물고기 번호 입력, 이전 위치 False
                    field[nx][ny], field[x][y] = f, False

                # 물고기가 있는 경우
                else:
                    # 상대 물고기 번호
                    op = field[nx][ny]
                    # 위치 바꿈
                    field[nx][ny], field[x][y] = field[x][y], field[nx][ny]
                    # 상대 물고기 위치 갱신

                    info[op] = [x, y, info[op][2]]

                # 현재 물고기 정보 수정
                info[f] = [nx, ny, (d+idx)%8]
                break
            else:
                idx += 1


    # 3. 상어 이동
    while True:
        r, c = r + dx[p], c + dy[p]
        # 상어가 이동할 수 있고, 해당 위치에 물고기가 있다면
        if 0 <= r < 4 and 0 <= c < 4:
            if field[r][c]:
                move([row[:] for row in field], r, c, p, info[:], res)
        else:
            global answer
            answer = max(answer, res)
            return


answer = 0
move(sea, 0, 0, 0, fishes, 0)
print(answer)