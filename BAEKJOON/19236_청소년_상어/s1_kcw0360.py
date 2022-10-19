import copy, sys
input = sys.stdin.readline


arr = [[0]*4 for _ in range(4)]
answer = 0
for i in range(4):
    ip = list(map(int, input().split()))
    for j in range(4):
        arr[i][j] = [ip[j*2], ip[j*2+1]-1]    # 각 위치의 물고기 정보 [번호, 방향]

# 문제에서 주어진 번호 순서대로 방향
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]


def dfs(fish, now_y, now_x, eat):
    global answer

    eat += fish[now_y][now_x][0]    # 물고기 잡아 먹기
    answer = max(answer, eat)    # 먹은 물고기 최대값 갱신
    fish[now_y][now_x][0] = 0    # 잡아먹은 물고기 위치는 빈칸으로 만들기

    # 물고기 번호순으로 위치를 찾은 후 이동
    for num in range(1, 17):
        a, b = -1, -1
        for i in range(4):
            for j in range(4):
                if fish[i][j][0] == num:
                    a, b = i, j
                    break

        if a == -1 and b == -1:    # 없는 번호는 skip
            continue

        d = fish[a][b][1]
        for k in range(8):
            y = a + dy[d]
            x = b + dx[d]

            if not (0 <= y < 4 and 0 <= x < 4) or (y == now_y and x == now_x):
                d = (d + 1) % 8    # 조건에 해당하지 않으면 방향 전환
                continue

            fish[a][b][1] = d
            fish[a][b], fish[y][x] = fish[y][x], fish[a][b]
            break

    # 상어 위치 이동
    nd = fish[now_y][now_x][1]
    for _ in range(4):
        now_y += dy[nd]
        now_x += dx[nd]

        if 0 <= now_y < 4 and 0 <= now_x < 4:
            if fish[now_y][now_x][0]:
                dfs(copy.deepcopy(fish), now_y, now_x, eat)


dfs(arr, 0, 0, 0)
print(answer)