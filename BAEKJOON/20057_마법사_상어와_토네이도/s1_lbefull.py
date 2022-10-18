import sys
input = sys.stdin.readline


def move(r, c, d):
    global answer
    nr = r + dr[d]                                  # 현재 방향으로 1 이동
    nc = c + dc[d]
    a = total = arr[nr][nc]                         # 이동한 위치의 총 모래양과 a를 초기화
    arr[nr][nc] = 0                                 # 이동한 위치 모래를 없애줌
    sandlist = [[nr + dr[d] * 2, nc + dc[d] * 2], [nr + dr[d] if dr[d] else nr + 1, nc + dc[d] if dc[d] else nc + 1], [nr + dr[d] if dr[d] else nr - 1, nc + dc[d] if dc[d] else nc - 1],
                [nr if dr[d] else nr + 1, nc if dc[d] else nc + 1], [nr if dr[d] else nr - 1, nc if dc[d] else nc - 1], [nr if dr[d] else nr + 2, nc if dc[d] else nc + 2], [nr if dr[d] else nr - 2, nc if dc[d] else nc - 2],
                [nr - dr[d] if dr[d] else nr + 1, nc - dc[d] if dc[d] else nc + 1], [nr - dr[d] if dr[d] else nr - 1, nc - dc[d] if dc[d] else nc - 1]]

    for i in range(9):                              # sandlist에는 모래가 퍼지는 좌표를 담아줌
        sr = sandlist[i][0]                         # a를 제외한 모래가 퍼지는 9개 범위를 탐색
        sc = sandlist[i][1]
        amount = total * sand[i] // 100             # 비율만큼 모래를 구해줌
        a -= amount                                 # a에서 모래양을 빼주고
        if 0 <= sr < N and 0 <= sc < N:             # 인덱스 범위 내라면 해당 위치에 추가하고
            arr[sr][sc] += amount                   # 인덱스를 벗어나면 answer에 추가
        else:
            answer += amount
    sr = nr + dr[d]
    sc = nc + dc[d]
    if 0 <= sr < N and 0 <= sc < N:                 # 마지막 a위치도 마찬가지로 추가
        arr[sr][sc] += a
    else:
        answer += a
    return nr, nc


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [0, 1, 0, -1]
dc = [-1, 0, 1, 0]
sand = [5, 10, 10, 7, 7, 2, 2, 1, 1]                # 모래가 퍼지는 비율을 sandlist와 인덱스가 맞게 저장

answer = 0
r = c = N // 2                                      # 시작점
k = 1                                               # 현재 방향으로 가야하는 거리
cnt = d = 0
while r != 0 or c != 0:                             # 0, 0이 되면 반복 종료
    r, c = move(r, c, d)                            # 현재 위치와 방향을 넣어주고 새로운 위치를 받음
    cnt += 1                                        # 이동 회수 + 1
    if cnt % k == 0:                                # 현재 방향으로 k만큼 갔다면
        d = (d + 1) % 4                             # 방향을 바꿔줌
        if cnt // k == 2:                           # 방향을 2번 바꿨따면
            cnt = 0                                 # cnt 초기화
            k += 1                                  # 가야할 거리 + 1

print(answer)
