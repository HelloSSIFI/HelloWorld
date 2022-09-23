n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

knights = []
chess = [[[] for _ in range(n)] for _ in range(n)]
for h in range(k):
    a, b, p = map(int, input().split())
    knights.append([a-1, b-1, p-1])
    chess[a-1][b-1].append(h)

# 번호별 말 해당 말 위에 있는 말 리스트
direct = [(0, 1), (0, -1), (-1, 0), (1, 0)]
turn = 0


def moving(reverse):
    Q = list()
    while chess[r][c]:
        tmp = chess[r][c].pop()
        Q.append(tmp)
        if tmp == i:
            break

    if reverse:
        while Q:
            el = Q.pop(0)
            knights[el] = [nr, nc, knights[el][2]]
            chess[nr][nc].append(el)
    else:
        while Q:
            el = Q.pop()
            knights[el] = [nr, nc, knights[el][2]]
            chess[nr][nc].append(el)


def change():
    global d, nr, nc

    if d == 0: d = 1
    elif d == 1: d = 0
    elif d == 2: d = 3
    else: d=2

    # 방향 전환
    nr, nc = r + direct[d][0], c + direct[d][1]

    # 격자 안이면
    if 0 <= nr < n and 0 <= nc < n:

        if arr[nr][nc] == 0:
            moving(False)
        elif arr[nr][nc] == 1:
            moving(True)
        else:
            nr, nc = r, c
    # 격자 밖이면 방향만 바꿔서 저장
    else:
        nr, nc = r, c

    knights[i] = [nr, nc, d]


while turn <= 1000:
    turn += 1
    for i in range(k):
        r, c, d = knights[i]
        nr, nc = r + direct[d][0], c + direct[d][1]

        if 0 <= nr < n and 0 <= nc < n:

            # 흰색일 때
            if arr[nr][nc] == 0:
                moving(False)

            # 빨강일 때
            elif arr[nr][nc] == 1:
                moving(True)

            # 파랑일 때
            else:
                change()
        else:
            change()

        if len(chess[nr][nc]) >= 4:
            print(turn)
            exit()

else:
    print(-1)