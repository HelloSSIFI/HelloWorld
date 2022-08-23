import sys
input = sys.stdin.readline

dr = [-1, 0, 1, 0]                                      # 시계방향
dc = [0, 1, 0, -1]
result = []
fb = {'F': 1, 'B': -1}

for _ in range(int(input())):
    ctrls = input().strip()                             # 명령을 입력받음
    min_r = max_r = min_c = max_c = r = c = d = 0

    for ctrl in ctrls:
        if ctrl in 'FB':                                # 전진 혹은 후진일 경우
            r += dr[d] * fb[ctrl]                       # 현재 바라보는 방향에 맞게 움직여줌
            c += dc[d] * fb[ctrl]
            max_r = max(max_r, r)                       # 현재 위치를 기준으로 최대, 최소 r, c 값을 갱신
            min_r = min(min_r, r)
            max_c = max(max_c, c)
            min_c = min(min_c, c)

        elif ctrl == 'L':                               # L 명령일 경우 d를 반시계방향으로 90도 돌려줌(d - 1)
            d = (d - 1) % 4

        else:                                           # R 명령일 경우 d를 시계방향으로 90도 돌려줌(d + 1)
            d = (d + 1) % 4
    result.append((max_r - min_r) * (max_c - min_c))

*map(print, result),
