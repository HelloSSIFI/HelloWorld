def solution(line):
    temp = [[], []]
    res = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]

            if A*D - B*C:    # 분모가 0이 아닌 경우에만 해를 구할 수 있다
                x = (B*F - E*D) / (A*D - B*C)    # x좌표 값
                y = (E*C - A*F) / (A*D - B*C)    # y좌표 값

                if x != int(x) or y != int(y):    # 정수가 아닌 경우 제외
                    continue

                temp[0].append(int(x))    # x좌표 저장
                temp[1].append(int(y))    # y좌표 저장
                res.append([int(x), int(y)])    # 교점 저장

    min_x, max_x, min_y, max_y = min(temp[0]), max(temp[0]), min(temp[1]), max(temp[1])    # 교점 x, y좌표 위치의 최대값, 최소값 찾기
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]    # 교점 찍을 좌표 생성

    for x, y in res:    # 교점에 별 찍기
        answer[max_y - y][x - min_x] = '*'

    return [''.join(s) for s in answer]