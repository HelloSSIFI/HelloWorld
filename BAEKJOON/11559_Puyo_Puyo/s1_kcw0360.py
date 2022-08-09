import sys
from collections import deque
input = sys.stdin.readline


puyo = [list(input()) for _ in range(12)]
answer = 0

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def crush(a, b, c):
    q = deque()
    visited = [[0]*6 for _ in range(12)]
    q.append([a, b])
    temp = [[a, b]]
    visited[a][b] = 1

    while q:
        y, x = q.popleft()

        for k in range(4):
            i = y + dy[k]
            j = x + dx[k]

            if 0 <= i < 12 and 0 <= j < 6 and puyo[i][j] == c and visited[i][j] == 0:
                visited[i][j] = 1
                temp.append([i, j])
                q.append([i, j])

    if len(temp) > 3:
        for i in temp:
            puyo[i[0]][i[1]] = '.'
        return 1
    return 0


def fill():
    for j in range(6):
        check = []
        for i in range(11, -1, -1):
            if puyo[i][j] != '.':
                check.append(puyo[i][j])
                puyo[i][j] = '.'
        for p in range(len(check)):
            puyo[11 - p][j] = check[p]


while True:
    tmp = []
    check = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                tmp.append([i, j])

    for n in tmp:
        check += crush(n[0], n[1], puyo[n[0]][n[1]])

    if check:
        fill()
        answer += 1
    else:
        break

print(answer)