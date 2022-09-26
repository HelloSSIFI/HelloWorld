def solution(line):
    points = []
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float(float('-inf')), float('-inf')
    for i in range(len(line)):
        a, b, e = line[i][0], line[i][1], line[i][2]
        for j in range(i+1, len(line)):
            c, d, f = line[j][0], line[j][1], line[j][2]

            if (a*d) - (b*c) != 0:
                x = ((b * f) - (e * d)) / ((a * d) - (b * c))
                y = ((e * c) - (a * f)) / ((a * d) - (b * c))
                if float.is_integer(x) and float.is_integer(y):
                    x, y = int(x), int(y)
                    points.append([y, x])
                    min_x, min_y = min(min_x, x), min(min_y, y)
                    max_x, max_y = max(max_x, x), max(max_y, y)
    answer = []
    for i in range(len(points)):
        r, c = points[i][0], points[i][1]
        r = r - min_y
        c = c - min_x
        points[i] = [r, c]
    for i in range(abs(max_y-min_y), -1, -1):
        s = ''
        for j in range(abs(max_x-min_x)+1):
            if [i, j] in points:
                s += '*'
            else:
                s += '.'
        answer.append(s)

    return answer


print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
print(solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]]))
print(solution([[1, -1, 0], [2, -1, 0]]))
print(solution([[1, -1, 0], [2, -1, 0], [4, -1, 0]]))
