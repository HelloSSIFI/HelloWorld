import sys
input = sys.stdin.readline


R, C, T = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(R)]
air_cleaner = []    # 공기 청정기 좌표 [위쪽, 아래쪽]
for i in range(R):
    if room[i][0] == -1:
        air_cleaner = [i, i+1]
        break

for _ in range(T):
    # 미세먼지 좌표 찾기
    q = []
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:
                q.append([i, j, room[i][j]])

    # 미세먼지 확산
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    while q:
        a, b, dust = q.pop()
        move = 0
        tmp = dust // 5
        for k in range(4):
            y = a + dy[k]
            x = b + dx[k]

            if 0 <= y < R and 0 <= x < C and room[y][x] != -1:
                move += 1
                room[y][x] += tmp

        room[a][b] -= (tmp * move)
    # 정화
    # 위쪽
    start = air_cleaner[0]
    tmp1 = 0    # 이전 칸 저장
    tmp2 = 0    # 현재 칸 저장
    for a in range(1, C):
        tmp1 = tmp2
        tmp2 = room[start][a]
        room[start][a] = tmp1
    for b in range(start-1, -1, -1):
        tmp1 = tmp2
        tmp2 = room[b][C-1]
        room[b][C-1] = tmp1
    for c in range(C-2, -1, -1):
        tmp1 = tmp2
        tmp2 = room[0][c]
        room[0][c] = tmp1
    for d in range(1, start):
        tmp1 = tmp2
        tmp2 = room[d][0]
        room[d][0] = tmp1

    # 아래쪽
    start = air_cleaner[1]
    tmp1 = 0
    tmp2 = 0
    for a in range(1, C):
        tmp1 = tmp2
        tmp2 = room[start][a]
        room[start][a] = tmp1
    for b in range(start+1, R):
        tmp1 = tmp2
        tmp2 = room[b][C-1]
        room[b][C-1] = tmp1
    for c in range(C-2, -1, -1):
        tmp1 = tmp2
        tmp2 = room[R-1][c]
        room[R-1][c] = tmp1
    for d in range(R-2, start, -1):
        tmp1 = tmp2
        tmp2 = room[d][0]
        room[d][0] = tmp1

result = 2    # 공기 청정기가 -2 이므로 초기값을 2로 둔다
for i in range(R):
    result += sum(room[i])

print(result)