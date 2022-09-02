import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())
arr = [list(map(lambda x: [int(x), 0], input().split())) for _ in range(n)]

drct = [(0, 1), (-1, 0), (0, -1), (1, 0)]
dcrt = [(0, 1), (1, 0), (0, -1), (-1, 0)]
purify = 0
for tc in range(t):

    for i in range(n):
        for j in range(m):
            if arr[i][j][0] == -1 and not purify:
                purify = i
                continue

            if arr[i][j][0] > 4:
                # dust = arr[i][j][2]
                cnt = 0     # 확산된 방향의 수

                for d in drct:
                    si, sj = i+d[0], j+d[1]
                    if 0 <= si < n and 0 <= sj < m and arr[si][sj][0] != -1:
                        cnt += 1
                        arr[si][sj][1] += arr[i][j][0]//5

                arr[i][j][0] -= (arr[i][j][0]//5)*cnt


    for i in range(n):
        for j in range(m):
            tmp = sum(arr[i][j])
            if tmp:
                arr[i][j] = [tmp, 0]

    ur, uc = purify, 0
    dr, dc = ur+1, 0
    position = (ur, dr)
    utmp, dtmp = 0, 0
    udx, ddx = 0, 0


    while udx < 4:
        if 0 <= ur+drct[udx][0] <= position[0] and 0 <= uc+drct[udx][1] < m:
            ur, uc = ur+drct[udx][0], uc+drct[udx][1]
            arr[ur][uc][0], utmp = utmp, arr[ur][uc][0]

        else:
            udx += 1

    else:
        arr[ur][uc][0] = -1
        utmp = 0


    while ddx < 4:
        if position[1] <= dr+dcrt[ddx][0] < n and 0 <= dc+dcrt[ddx][1] < m:
            dr, dc = dr+dcrt[ddx][0], dc+dcrt[ddx][1]
            arr[dr][dc][0], dtmp = dtmp, arr[dr][dc][0]

        else:
            ddx += 1

    else:
        arr[dr][dc][0] = -1
        dtmp = 0


answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j][0] > 0: answer += arr[i][j][0]
print(answer)