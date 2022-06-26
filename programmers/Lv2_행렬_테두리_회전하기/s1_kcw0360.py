def rotation(q, temp):
    a, b, c, d = q
    check = 0
    row = b - 2
    col = a - 1
    moving = 1
    fst = temp[a][b - 1]
    num1 = d - b + 1
    num2 = c - a
    ans = []
    while check < 2:
        for i in range(num1):
            row += moving
            snd = temp[col][row]
            temp[col][row] = fst
            ans.append(fst)
            fst = snd
        num1 -= 1

        for j in range(num2):
            col += moving
            snd = temp[col][row]
            temp[col][row] = fst
            ans.append(fst)
            fst = snd
        num2 -= 1
        moving *= -1
        check += 1
    return min(ans), temp


def solution(rows, columns, queries):
    answer = []
    temp = [[0] * columns for _ in range(rows)]
    cnt = 1

    for i in range(rows):
        for j in range(columns):
            temp[i][j] = cnt
            cnt += 1

    for i in queries:
        ans, temp = rotation(i, temp)
        answer.append(ans)
    return answer