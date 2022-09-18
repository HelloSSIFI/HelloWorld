from collections import deque, defaultdict


def solution(rectangle, characterX, characterY, itemX, itemY):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    point = []                                                      # i번째 사각형의 4개의 꼭지점을 각각 set으로 저장
    init_rec = 0                                                    # 초기 x가 가장 작은 사각형의 y값과 사각형 번호를 저장
    init_x = 50
    init_y = 50
    for lx, ly, rx, ry in rectangle:
        if lx < init_x:                                             # x가 가장 작은 사각형 갱신
            init_x = lx
            init_y = ly
            init_rec = len(point)
        temp = set()
        for x, y in [[lx, ly], [lx, ry], [rx, ly], [rx, ry]]:       # 4개의 꼭지점을 저장
            temp.add((x, y))
        point.append(temp)
    
    conn = defaultdict(set)                                         # 두 사각형의 접점을 key로 하여 두 사각형 인덱스를 set으로 저장
    for i in range(len(rectangle) - 1):
        lx, ly, rx, ry = rectangle[i]
        pos = set()
        for x in range(lx, rx + 1):                                 # 우선 i번 사각형의 모든 둘레의 좌표를 저장
            pos.update({(x, ly), (x, ry)})
        for y in range(ly, ry + 1):
            pos.update({(lx, y), (rx, y)})
        
        for j in range(i + 1, len(rectangle)):                      # i와 다른 j번 사각형의 둘레를 돌면서
            lx2, ly2, rx2, ry2 = rectangle[j]                       # 이미 i번 사각형에서 나온 좌표이면
            for x2 in range(lx2, rx2 + 1):                          # 해당하는 점을 key로하여 i와 j를 셋에 넣어줌
                if (x2, ly2) in pos:
                    conn[(x2, ly2)].update({i, j})
                if (x2, ry2) in pos:
                    conn[(x2, ry2)].update({i, j})
            for y2 in range(ly2, ry2 + 1):
                if (lx2, y2) in pos:
                    conn[(lx2, y2)].update({i, j})
                if (rx2, y2) in pos:
                    conn[(rx2, y2)].update({i, j})

    answer = 2501
    for d, a in [[0, 1], [1, -1]]:                                  # 위에서 구한 초기값에서 시계방향과 반시계방향으로 각각 돌아줌
        x = init_x                                                  # 초기값을 받아옴
        y = init_y
        rec = init_rec
        flag = True                                                 # 캐릭터 위치가 발견되기 전까지 True
        cnt = 0                                                     # 캐릭터 위치가 발견된 후부터 카운트
        while flag or x != itemX or y != itemY:                     # 캐릭터 위치를 발견한 후 아이템위치를 발견할 때까지 반복
            if x == characterX and y == characterY:                 # 캐릭터 위치이면 flag를 False로 바꿔 카운트 시작
                flag = False
            x += dx[d]                                              # 좌표 갱신
            y += dy[d]
            if (x, y) in conn:                                      # 두 사각형이 만나는 지점이면
                d = (d - a) % 4                                     # 방향을 사각형 기본 방향과 반대방향으로 바꿔줌
                for i in conn[(x, y)]:
                    if i != rec:
                        rec = i
                        break
            elif (x, y) in point[rec]:                              # 사각형의 모서리를 만난다면
                d = (d + a) % 4                                     # 방향을 사각형을 만드는 방향으로 바꿔줌
            if not flag:                                            # 캐릭터 위치가 발견되었다면 카운트
                cnt += 1
        answer = min(answer, cnt)
    return answer


# print(solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8))
