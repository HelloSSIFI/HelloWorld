import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
length = 2**N
ice = [list(map(int, input().split())) for _ in range(2**N)]
L_list = list(map(int, input().split()))

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for L in L_list:
    # 회전하기
    t = 2**L
    for i in range(0, length, t):
        for j in range(0, length, t):
            temp = [ice[_][j:j+t] for _ in range(i, i+t)]
            for n in range(t):
                for m in range(t):
                    ice[i+m][j+t-1-n] = temp[n][m]

    # temp에 인접한 얼음 갯수 표기
    temp = [[0]*length for _ in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(4):
                y = i + dy[k]
                x = j + dx[k]
                if 0 <= y < length and 0 <= x < length and ice[y][x]:
                    temp[i][j] += 1


    # 인접한 얼음 개수가 3개 미만 이면 얼음 녹이기
    for i in range(length):
        for j in range(length):
            if ice[i][j] > 0 and temp[i][j] < 3:
                ice[i][j] -= 1

print(sum(sum(i) for i in ice))    # 남은 얼음의 합

# 얼음 덩어리 찾기
ice_cube = 0
for i in range(length):
    for j in range(length):
        if ice[i][j]:
            q = [[i, j]]
            ice[i][j] = 0
            cnt = 1
            while q:
                a, b = q.pop()
                for k in range(4):
                    y = a + dy[k]
                    x = b + dx[k]
                    if 0 <= y < length and 0 <= x < length and ice[y][x]:
                        q.append([y, x])
                        ice[y][x] = 0
                        cnt += 1

            ice_cube = max(ice_cube, cnt)

print(ice_cube)