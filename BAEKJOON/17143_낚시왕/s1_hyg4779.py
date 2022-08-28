'''
사람 오른쪽으로 1칸씩 이동
같은열 가장 높은위치 행에 있는 상어 잡음 -> 상어 사라짐
상어 이동 -> 같은 칸에 있는 상어 중 가장 큰 상어가 나머지를 다 잡음
낚시왕이 잡은 상어 크기 합
'''
from collections import defaultdict
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [[0]*m for _ in range(n)]

shark_dict = defaultdict(list)
direct = [0, [-1, 0], [1, 0], [0, 1], [0, -1]]
sharks = [[] for _ in range(k)]

for l in range(k):
    r, c, s, d, z = map(int, input().split())
    arr[r-1][c-1] = z               # 격자에 상어 크기를 넣음
    sharks[l] = [r-1, c-1, z, s, d]

now = -1
answer = 0
while now < m-1:
    now += 1

    # 상어 잡기 pass
    for i in range(n):
        if arr[i][now]:
            answer += arr[i][now]
            arr[i][now] = 0
            break

    # 상어 이동
    for j in range(k):
        x, y, size, speed, d = sharks[j]
        # 속력이 0 or 먹혔으면 continue
        if speed == 0 or size==0:
            continue

        speed %= n-1
        sx, sy = x+direct[d][0]*speed, y+direct[d][1]*speed
        '''
        1. 이동해도 벽에 안 부딪힐 때
        2. 벽에 한 번 부딪힐 때
        3. 벽에 두 번 이상 부딪힐 때
        '''
        # 벽에 안 부딪힐 때
        if 0 <= sx < n and 0 <= sy < m:
            arr[x][y] -= size
            arr[sx][sy] += size
            sharks[j] = [sx, sy, size, speed, d]
        # 세로로 부딪힐 때
        elif d <= 2:
            sx = (n-1)-x

            arr[x][y] -= size
            arr[sx][sy] += size
            sharks[j] = [sx, sy, size, speed, d]
        # 가로로 부딪힐 때
        elif d >= 3:
            sy = (m-1)-y

            arr[x][y] -= size
            arr[sx][sy] += size
            sharks[j] = [sx, sy, size, speed, d]

    # 같은 위치 상어 지우기
    check = defaultdict(list)
    for l in range(k):
        a, b, size, speed, d = sharks[l]
        if size == 0:continue

        if not check[(a, b)]:
            check[(a, b)] = [size, l]

        else:
            # 지금 들어온 상어가 더 크다면 기존 상어 없앰
            if check[(a, b)][0] < size:
                pre = check[(a, b)][1]
                sharks[pre][2] = 0
                check[(a, b)] = [size, l]
                arr[a][b] = size

            # 기존 상어가 더 크다면 현재 상어 없앰
            else:
                arr[a][b] -= size
                sharks[l][2] = 0

print(answer)