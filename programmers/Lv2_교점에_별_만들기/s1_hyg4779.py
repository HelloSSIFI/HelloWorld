def solution(line):
    n = len(line)

    # 교점 구하기
    def dot(l1, l2):
        x1, y1, c1 = l1
        x2, y2, c2 = l2

        # 두 직선 평행 조건 == 만나지 않음
        if x1*y2 == y1*x2:
            return None

        # 평행하지 않는 두 직선의 교점
        a = (y1*c2 - y2*c1)/(x1*y2 - x2*y1)
        b = (x2*c1 - x1*c2)/(x1*y2 - x2*y1)
        # b = -(x1*c2 - x2*c1)/(x1*y2 - x2*y1)

        if a == int(a) and b == int(b):
            return (int(a), int(b))

    # 모든 직선들 조합
    all_comb = []
    for i in range(n-1):
        for j in range(i+1, n):
            all_comb.append([i, j])

    # 모든 정수 교점 추가
    points = list()
    for comb in all_comb:
        point = dot(line[comb[0]], line[comb[1]])
        if point != None:
            points.append(point)


    # 최소 최대 x, y 좌표 구하기
    X, Y = [r[0] for r in points], [c[1] for c in points]
    min_x, max_x, min_y, max_y = min(X), max(X), min(Y), max(Y)


    answer = ['.'*(max_x-min_x+1) for _ in range(max_y-min_y+1)]

    for x, y in points:
        answer[max_y-y] = answer[max_y-y][:x-min_x] + '*' + answer[max_y-y][x-min_x+1:]

    return [''.join(ans) for ans in answer]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))