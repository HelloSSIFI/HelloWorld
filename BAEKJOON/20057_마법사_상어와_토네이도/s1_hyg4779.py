import sys
sys.stdin = open('input.txt')

# 진행 방향에 따른 모래 날림
west = [
    [1, 0, 0.07],  # 수직 위아래 1칸 씩 7%
    [-1, 0, 0.07],
    [2, 0, 0.02],  # 수직 위아래 2칸 씩 2%
    [-2, 0, 0.02],
    [-1, -1, 0.1],  # 앞 대각 10% / east는 *(-1)
    [1, -1, 0.1],
    [1, 1, 0.01],  # 뒤 대각 1% / east는 *(-1)
    [-1, 1, 0.01],
    [0, -2, 0.05],  # 정면 2칸 / east는 *(-1)
    [0, -1],  # 정면 1칸 /east는 *(-1)
]

south = [
    [0, 1, 0.07],  # 수직 위아래 1칸 씩 7%
    [0, -1, 0.07],
    [0, 2, 0.02],  # 수직 위아래 2칸 씩 2%
    [0, -2, 0.02],
    [1, -1, 0.1],  # 앞 대각 10% / north는 *(-1)
    [1, 1, 0.1],
    [-1, -1, 0.01],  # 뒤 대각 1% / north는 *(-1)
    [-1, 1, 0.01],
    [2, 0, 0.05],  # 정면 2칸 / north는 *(-1)
    [1, 0],  # 정면 1칸 / north는 *(-1)
]

'''
반시계 방향으로 토네이도를 돌 때,
진행 방향의 다음 방향이 비었다면 돈다
1. 움직임
2. 움직인 위치에서 토네이도
'''

def tornado(r, c, p, rotate):  # 현재위치 행/열, 방향, west or south
    global result
    sand = 0
    dummy = matrix[r][c]
    for now, line in enumerate(rotate):

        if now >= 4 and p in (2, 3):  # 동 or 북
            ni, nj = r - line[0], c - line[1]


        else:  # 서 or 남
            ni, nj = r + line[0], c + line[1]

        if now == 9:
            dust = int(dummy - sand)
        else:
            dust = int(dummy * line[2])
        # dust = int(dust)
        if 0 <= ni < N and 0 <= nj < N:  # 모래바람이 격자 안이라면
            matrix[ni][nj] += dust

        else:  # 모래가 격자 밖으로 나갔을 때
            result += dust

        sand += dust

# 항상 홀 수
N = int(input())

# 모래격자
matrix = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*N for _ in range(N)]
# 시작위치
si, sj = N // 2, N // 2

visit[si][sj] = True
# 진행방향 서남동북
di = [0, 1, 0, -1]
dj = [-1, 0, 1, 0]

# 최종결과
result = 0

# 격자를 채운 횟 수
cnt = 0
# 현재 방향
idx = 0 # 서 남 동 북
visit[si][sj] = True
while cnt <= N ** 2 - 2:

    # 움직임
    si, sj = si + di[idx], sj + dj[idx]

    # 방문 처리
    visit[si][sj] = True

    # 토네이도
    if idx == 0 or idx == 2:  # 동서
        tornado(si, sj, idx, west)

    else:  # 남북
        tornado(si, sj, idx, south)

    cnt += 1
    # 방향 전환 가능한지 확인
    # 방향 전환 했을때 예상 위치
    ti = si + di[(idx+1)%4]
    tj = sj + dj[(idx+1)%4]

    if 0 <= ti < N and 0 <= tj < N and visit[ti][tj] == False:  # 방향 전환시 위치가 비어있다면면
        idx = (idx+1)%4    # 방향 전환

else:
    print(int(result))