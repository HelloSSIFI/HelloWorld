import sys
input = sys.stdin.readline


N, M = map(int, input().split())
basket = [list(map(int, input().split())) for _ in range(N)]
move_info = [list(map(int, input().split())) for _ in range(M)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

# 방향
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
direction = [1, 3, 5, 7]    # 대각선 방향 번호

for m in range(M):
    # 구름 이동 및 물의 양 1 증가 (조건 1, 2)
    move = set()
    for a, b in cloud:
        y = (a + dy[move_info[m][0]-1] * move_info[m][1]) % N
        x = (b + dx[move_info[m][0]-1] * move_info[m][1]) % N
        move.add((y, x))
        basket[y][x] += 1

    # 물복사버그 마법 (조건 4)
    for a, b in move:
        cnt = 0
        for d in direction:
            y = a + dy[d]
            x = b + dx[d]
            if 0 <= y < N and 0 <= x < N and basket[y][x]:
                cnt += 1
        basket[a][b] += cnt

    # 구름 생성 (조건 5)
    cloud = []
    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and ((i, j) not in move):
                cloud.append((i, j))
                basket[i][j] -= 2

answer = 0
for b in basket:
    answer += sum(b)

print(answer)