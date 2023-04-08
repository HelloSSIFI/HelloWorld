from collections import deque
import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
shark = [N//2, N//2]
tornado = []    # 상어 기준으로 구슬을 체크하기 위한 좌표를 순서대로 저장

def road():    # tornado에 좌표를 넣어준다.
    y, x = N//2, N//2
    move = 0

    # 방향
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    while True:
        for k in range(4):
            if k%2 == 0:
                move += 1

            for _ in range(move):
                y += dy[k]
                x += dx[k]
                tornado.append([y, x])
                if y == 0 and x == 0:
                    return

road()
length = len(tornado)

def fill_blanks():    # 빈칸 채우기
    beads = deque()
    for y, x in tornado:
        if arr[y][x]:
            beads.append(arr[y][x])

    for y, x in tornado:
        if beads:
            arr[y][x] = beads.popleft()
        else:
            arr[y][x] = 0

def check(num, cnt):    # 구슬 번호에 맞게 개수 추가
    if num == 1:
        result[0] += cnt
    elif num == 2:
        result[1] += cnt
    elif num == 3:
        result[2] += cnt

def bomb_beads():    # 구슬 폭파
    total = 0
    num, cnt = arr[tornado[0][0]][tornado[0][1]], 1
    bomb = [tornado[0]]
    for idx in range(1, length):
        if num != arr[tornado[idx][0]][tornado[idx][1]]:
            if num and cnt >= 4:
                total += 1
                check(num, cnt)
                for a, b in bomb:
                    arr[a][b] = 0
            num = arr[tornado[idx][0]][tornado[idx][1]]
            bomb = []
            cnt = 0
        bomb.append(tornado[idx])
        cnt += 1

    if num and cnt >= 4:
        total += 1
        check(num, cnt)
        for a, b in bomb:
            arr[a][b] = 0

    return total

# 블리자드 마법 방향
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, -1, 1]

result = [0, 0, 0]
for m in range(M):
    d, s = map(int, input().split())
    for k in range(1, s+1):    # 블리자드로 구슬 파괴
        y, x = shark[0] + dy[d]*k , shark[1] + dx[d]*k
        arr[y][x] = 0

    fill_blanks()    # 빈칸 채우기

    while True:    # 구슬 폭파 -> 구슬 채우기 루틴을 폭파하는 구슬이 없을때 까지 반복
        if bomb_beads():
            fill_blanks()
        else:
            break

    # 구슬 색깔별로 카운팅 한 후, 구슬 번호 바뀔 때 마다 temp에 넣어준다.
    num, cnt = arr[tornado[0][0]][tornado[0][1]], 1
    temp = deque()
    for idx in range(1, length):
        if num != arr[tornado[idx][0]][tornado[idx][1]]:
            temp.append(cnt)
            temp.append(num)
            num = arr[tornado[idx][0]][tornado[idx][1]]
            cnt = 0
        cnt += 1
    if num:
        temp.append(cnt)
        temp.append(num)

    # temp에 넣었던 값들을 순서대로 꺼내서 arr에 좌표에 맞게 값을 넣어준다. 더 이상 없다면 0을 넣어준다.
    for y, x, in tornado:
        if temp:
            arr[y][x] = temp.popleft()
        else:
            arr[y][x] = 0

answer = 0
for i in range(3):    # 결과값 계산
    answer += (i+1) * result[i]

print(answer)