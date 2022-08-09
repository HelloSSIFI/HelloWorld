from collections import deque

arr = [list(input()) for _ in range(12)]
answer = 0
direct = [(1, 0), (-1, 0), (0, -1), (0, 1)]

while True:
    boom = list()
    visit = [[0]*6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and not visit[i][j]:
                color, cnt, visit[i][j] = arr[i][j], 0, 1
                Q = deque([(i, j)])
                group = list()
                while Q:
                    r, c = Q.popleft()
                    group.append((r, c))
                    cnt += 1
                    for d in direct:
                        dr, dc = r+d[0], c+d[1]
                        if 0 <= dr < 12 and 0 <= dc < 6 and arr[dr][dc] == color and not visit[dr][dc]:
                            visit[dr][dc] = 1
                            Q.append((dr, dc))
                if cnt >= 4:
                    boom.append(group)

    if not boom:
        break
    for b in boom:
        for p, y in b:
            arr[p][y] = '.'
    answer += 1
    while True:
        flag = True
        for r in range(11):
            for c in range(6):
                if arr[r][c] != '.' and arr[r+1][c] == '.':
                    arr[r][c], arr[r+1][c] = arr[r+1][c], arr[r][c]
                    flag = False
        if flag:
            break

print(answer)
