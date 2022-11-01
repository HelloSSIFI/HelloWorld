'''
m, n = map(int, input().split())
gallery = [list(input()) for _ in range(m)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


# 격자안 판별 함수
def in_map(r, c):
    return True if 0 <= r < m and 0 <= c < n else False


# 빈칸 판별 함수
def is_blank(r, c):
    return True if gallery[r][c] == '.' else False


# 벽위치와 바라보는 방향 해싱 함수
def hashing(r, c, d):
    return str(r) + str(c) + str(d)


using = dict()
wall = 0

# 4방향 탐색
for k in [1, 3]:

    for i in range(m):
        for j in range(n):
            # 벽일때
            if gallery[i][j] == 'X':

                # 현재 벽의 탐색 방향이 사용중이라면 continue
                if using.get(hashing(i, j, k), 0): continue

                ni, nj = i + dx[k], j + dy[k]
                # 격자 안이고, 인접한 곳이 벽일 때
                if in_map(ni, nj) and gallery[ni][nj] == 'X':

                    # 두 벽의 수직 방향
                    if k <= 1:
                        turn = [2, 3]

                    else:
                        turn = [0, 1]

                    for l in turn:
                        x1, y1 = i + dx[l], j + dy[l]

                        x2, y2 = ni + dx[l], nj + dy[l]

                        # 탐색 중인 벽의 방향이 사용중이라면 continue
                        if using.get(hashing(i, j, l), 0) or using.get(hashing(ni, nj, l), 0):
                            continue

                        # 수직 방향이 격자 밖이면 continue
                        if not in_map(x1, y1) and not in_map(x2, y2):
                            continue

                        # 수직 칸 모두 빈칸이라면
                        if is_blank(x1, y1) and is_blank(x2, y2):
                            using[hashing(i, j, l)] = 1
                            using[hashing(ni, nj, l)] = 1
                            wall += 1


print(wall)
'''
n, m = map(int, input().split())
gallery = [list(input()) for _ in range(n)]

answer = 0


def pic(obj1, obj2, n, m, x, y):
    global answer
    rc = [0, 0]
    for rc[x] in range(n-1):
       cnt = 0
       for rc[y] in range(m):
           if gallery[rc[0]][rc[1]] == obj1 and gallery[rc[0]+y][rc[1]+x] == obj2:
               cnt += 1
           else:
                answer += cnt // 2
                cnt = 0

for obj1, obj2 in [['X', '.'], ['.', 'X']]:
    pic(obj1, obj2, n, m, 0, 1)
    pic(obj1, obj2, m, n, 1, 0)

print(answer)