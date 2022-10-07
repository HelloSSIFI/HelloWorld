import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
nutrients = [[5]*N for _ in range(N)]
nutrients_injection = []
for _ in range(N):
    nutrients_injection.append(list(map(int, input().split())))
woods = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    woods[x-1][y-1].append(z)
    woods[x-1][y-1].sort()

# K년 지날 때 까지 사계절 반복
for _ in range(K):
    # 나무에 양분 주입
    for i in range(N):
        for j in range(N):
            if woods[i][j]:
                woods[i][j].sort()
                temp, die = [], 0
                for age in woods[i][j]:
                    if age <= nutrients[i][j]:
                        nutrients[i][j] -= age
                        age += 1
                        temp.append(age)
                    else:
                        die += age // 2

                nutrients[i][j] += die
                woods[i][j] = temp

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    # 번식
    for i in range(N):
        for j in range(N):
            if woods[i][j]:
                for w in woods[i][j]:
                    if w % 5 == 0:
                        for k in range(8):
                            y = i + dy[k]
                            x = j + dx[k]
                            if 0 <= y < N and 0 <= x < N:
                                woods[y][x] = [1] + woods[y][x]

    # 땅에 양분 주입
    for i in range(N):
        for j in range(N):
            nutrients[i][j] += nutrients_injection[i][j]

# 각 위치의 나무 개수 answer에 더하기
answer = 0
for a in range(N):
    for b in range(N):
        if woods[a][b]:
            answer += len(woods[a][b])

print(answer)