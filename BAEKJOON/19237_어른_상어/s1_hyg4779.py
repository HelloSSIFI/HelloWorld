n, m, k = map(int, input().split())

dx = (0, -1, 1, 0, 0)
dy = (0, 0, 0, -1, 1)

sharks = dict()
field = [[0]*n for _ in range(n)]
smell = [[0]*n for _ in range(n)]
smells = dict()
# 상어들 위치 정보 및 냄새 뿌리기
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j]:
            sharks[line[j]] = (i, j)
            smells[(i, j)] = [line[j], k]
            smell[i][j] = line[j]
            field[i][j] = k

# 상어 번호 별 현재 방향
head = [0] + list(map(int, input().split()))

# 상어 번호 별 방향에 따른 우선순위
direct = dict()
for num in range(1, m+1):
    direct[num] = [[], ]
    for _ in range(4):
        direct[num].append(list(map(int, input().split())))

time = 0

while time < 1000:
    time += 1
    # 상어 이동
    for num in range(1, m+1):
        # 죽은상어 pass
        if sharks[num]==False:
            continue

        # 현재 위치와, 우선순위 방향
        r, c = sharks[num]
        move = direct[num][head[num]]

        for idx in move:
            nr, nc = r + dx[idx], c + dy[idx]
            # 격자 안이고 냄새 없는 칸 찾기
            if 0 <= nr < n and 0 <= nc < n and field[nr][nc] == 0:
                sharks[num] = (nr, nc)
                head[num] = idx
                break

        # 빈칸 못 찾았으면
        else:
            for idx in move:
                nr, nc = r + dx[idx], c + dy[idx]
                if 0 <= nr < n and 0 <= nc < n and smell[nr][nc] == num:
                    sharks[num] = (nr, nc)
                    head[num] = idx
                    break




    # 상어 겹치는 칸 찾기
    for high in range(1, m):
        if sharks[high] == False: continue
        for low in range(high+1, m+1):
            if sharks[high] == sharks[low]:
                sharks[low] = False

    # 냄새 한칸 -1
    for i in range(n):
        for j in range(n):
            if field[i][j]:
                field[i][j] -= 1
                if field[i][j] == 0:
                    smell[i][j] = 0


    # 냄새 뿌리기
    for s, p in sharks.items():
        if p == False:continue
        r, c = p
        field[r][c] = k
        smell[r][c] = s


    cnt = 0
    for s in sharks.values():
        if s:cnt+= 1

    if cnt == 1:
        print(time)
        break
else:
    print(-1)
