import sys
input = sys.stdin.readline

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
info = dict()
for n in range(K):
    r, c, di = map(int, input().split())
    chess[r-1][c-1].append(n)
    info[n] = [r-1, c-1, di-1]

d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

flag = False
turn = 0
while not flag:

    # for i in range(N):
    #     print(chess[i][:])
    # print(info)

    turn += 1
    if turn > 1000:
        turn = -1
        flag = True

    for k, v in info.items():
        i, j, di = v[0], v[1], v[2]
        # 위에 얹힌 체스말 확인
        index = chess[i][j].index(k)
        ni, nj = i + d[di][0], j + d[di][1]
        if 0 <= ni < N and 0 <= nj < N and color[ni][nj] != 2:
            pass
        else:
            if di in [0, 2]:
                di += 1
            else:
                di -= 1

            ni, nj = i + d[di][0], j + d[di][1]
        info[k][-1] = di

        # 파란색 진입
        if 0 > ni or ni >= N or 0 > nj or nj >= N or color[ni][nj] == 2:
            continue
        # 빨간색 진입
        elif color[ni][nj] == 1:
            ind = len(chess[i][j])-1
            while ind >= index:
                cn = chess[i][j].pop()
                chess[ni][nj].append(cn)
                info[cn][0], info[cn][1] = ni, nj
                ind -= 1
        else:
            ind = index
            l = len(chess[i][j])
            while ind < l:
                cn = chess[i][j].pop(index)
                chess[ni][nj].append(cn)
                info[cn][0], info[cn][1] = ni, nj
                ind += 1
        if len(chess[ni][nj]) >= 4:
            flag = True
            break

print(turn)
