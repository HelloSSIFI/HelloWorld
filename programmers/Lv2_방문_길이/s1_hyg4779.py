def solution(dirs):

    # 명령 별 이동 방향 (x좌표, y좌표)
    move = {
        'U': (0, -1),
        'D': (0, 1),
        'L': (-1, 0),
        'R': (1, 0)
    }

    # 방문한 길 set
    route = set()
    # 현재 좌표
    x, y = 0, 0

    for d in dirs:
        r, c = move[d]

        # 좌표평면 내
        if -5 <= x + r <= 5 and -5 <= y + c <= 5:
            # 해당 길을 방문한 적이 없다면 추가(현재 진행 방향, 반대 방향 검사)
            if ((x, y), (x+r,  y+c)) not in route and ((x+r,  y+c), (x, y)) not in route:
                route.add(((x, y), (x+r,  y+c)))

            # 좌표 수정
            x += r
            y += c

    return len(route)

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))