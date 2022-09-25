def solution(line):
    temp = [[], []]
    res = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            A, B, E = line[i]
            C, D, F = line[j]

            if A*D - B*C:
                x = (B*F - E*D) / (A*D - B*C)
                y = (E*C - A*F) / (A*D - B*C)

                if x != int(x) or y != int(y):
                    continue

                temp[0].append(int(x))
                temp[1].append(int(y))
                res.append([int(x), int(y)])

    min_x, max_x, min_y, max_y = min(temp[0]), max(temp[0]), min(temp[1]), max(temp[1])
    answer = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in res:
        answer[max_y - y][x - min_x] = '*'

    return [''.join(s) for s in answer]