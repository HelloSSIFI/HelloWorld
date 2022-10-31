# 격자 크기, m개의 나무, k년 후 살아있는 나무 print
n, m, k = map(int, input().split())

# 겨울에 추가 되는 칸 별 양분의 양
A = [list(map(int, input().split())) for _ in range(n)]

# 칸 별 양분 상태
nutrient = [[5]*n for _ in range(n)]

# 칸 별 나무의 수
field = [[[] for _ in range(n)] for _ in range(n)]

# 심은 나무의 위치
for _ in range(m):
    a, b, c = map(int, input().split())
    # 나무 추가
    field[a-1][b-1].append(c)
    field[a-1][b-1].sort()

# 나무 번식 8방향
direct = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

live = 0
while k:
    # 햇수 1 차감
    k -= 1
    # 현재 살아있는 나무 수
    live = 0

    # 봄
    for i in range(n):
        for j in range(n):
            # 나무 없는 칸은 continue
            if not field[i][j]:continue

            idx, l = 0, len(field[i][j])
            while idx < l:
                now = field[i][j][idx]
                # 양분이 나무 나이만큼 없다면 break하고 영양분 채우기
                if nutrient[i][j] < now:
                    break

                # 나이만큼 양분 먹고, 나무 나이 추가
                nutrient[i][j] -= now
                field[i][j][idx] += 1
                idx += 1

            # 여름 작업 진행: 죽은 나무 영양분 추가
            for x in range(idx, l):
                nutrient[i][j] += field[i][j][x]//2
            field[i][j] = field[i][j][:idx]

    # 가을
    for i in range(n):
        for j in range(n):
            # 나무 없는 곳 continue
            if not field[i][j]:continue
            for x in range(len(field[i][j])):
                if field[i][j][x]%5 == 0:
                    for d in direct:
                        ni, nj = i+d[0], j+d[1]
                        if 0 <= ni < n and 0 <= nj < n:
                            field[ni][nj] = [1]+field[ni][nj]

    # 겨울
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += A[i][j]
            live += len(field[i][j])


print(live)