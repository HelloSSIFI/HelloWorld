import sys
input = sys.stdin.readline


N = int(input())
sand = [list(map(int, input().split())) for _ in range(N)]

# 좌, 하, 우, 상
dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

# 이동 좌표 기준 모래 퍼지는 곳의 y, x 좌표와 비율
wind_y = [[-1, 1, -2, 2, 0, -1, 1, -1, 1], [-1, -1, 0, 0, 2, 0, 0, 1, 1],
          [1, -1, 2, -2, 0, 1, -1, 1, -1], [1, 1, 0, 0, -2, 0, 0, -1, -1]]
wind_x = [[1, 1, 0, 0, -2, 0, 0, -1, -1], [-1, 1, -2, 2, 0, -1, 1, -1, 1],
          [-1, -1, 0, 0, 2, 0, 0, 1, 1], [1, -1, 2, -2, 0, 1, -1, 1, -1]]
rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]


def wind(a, b, d):
    check = 0    # 모래 밭 밖으로 나간 양
    sw = sand[a][b]
    check_sum = 0    # 모래 바람으로 날아가는 모래의 총 양

    # 모래바람으로 퍼지는 각 위치 모래 체크
    for r in range(9):
        o, p = a + wind_y[d][r], b + wind_x[d][r]
        tor = (sw * rate[r]) // 100    # 모래 바람의 모래 양
        check_sum += tor    # 총 합 체크

        if 0 <= o < N and 0 <= p < N:    # 모래밭 안의 좌표인 경우
            sand[o][p] += tor    # 해당 좌표로 불어온 모래 추가
        else:
            check += tor    # 모래밭 밖의 좌표인 경우 체크에만 추가

    ny, nx = a + dy[d], b + dx[d]    # 다음 이동 경로
    temp = sand[a][b] - check_sum    # 현 위치의 모래 양에서 사라진 모래 제거

    if 0 <= ny < N and 0 <= nx < N:
        sand[ny][nx] += temp    # 다음 이동 장소에 모래 추가
    else:
        check += temp    # 모래 밭 밖인 경우

    sand[a][b] = 0    # 모래 소멸

    return check


answer = 0
visited = [[0]*N for _ in range(N)]
direction = -1

sy, sx = N//2, N//2
while True:
    if sy == 0 and sx == 0:
        break

    visited[sy][sx] = 1
    k = (direction + 1) % 4    # 방향 전환
    y, x = sy + dy[k], sx + dx[k]    # 다음 이동 좌표

    if visited[y][x]:    # 이동할 곳이 지나간 장소인 경우
        k = direction    # 방향을 원상 복구
        y, x = sy + dy[k], sx + dx[k]    # 다음 이동 좌표

    answer += wind(y, x, k)
    sy, sx, direction = y, x, k

print(answer)